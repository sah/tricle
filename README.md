# tricle

tricle is a python3 [monocle](http://github.com/saucelabs/monocle)
adapter, allowing monocle code ported from python2 to work with
minimal modifications, and to interoperate gracefully with python3's
native asyncio framework. It has two main goals:

1) Allow for a smooth, incremental transition away from monocle-based
code to native asyncio code.
2) Where monocle had significantly better ideas and APIs than are
available on asyncio, continue to refine those components to be useful
to all users of asyncio.

Monocle behaviors are copied closely, but not exactly — object APIs,
exceptions raised, and other details may differ in some cases. The
hope here is to make porting monocle code easy, but not necessarily
automatic. We want to encourage migration to native asyncio code, so
tricle at times tries to expose underlying asyncio APIs and mechanisms
rather than wrap them completely.  Some more essoteric monocle
functionality may not be copied, especially where asyncio alternatives
exist.

Example interoperation with asyncio:

    # monocle oroutines work unmodified:
    @_o
    def slow_square(x):
        yield monocle.util.sleep(x)
        yield Return(x * x)

    # here's how to do something similar with asyncio and python3 async/await syntax:
    async slow_cube(x):
        await asyncio.sleep(x)
        return x * x * x
        
    # monocle oroutines can yield to native coroutines seamlessly:
    @_o
    def slow_sixth_power(x):
        yield asyncio.sleep(x)  # monocle.util.sleep is in fact this same function
        y = yield slow_cube(x * x)
        yield Return(y)
        
    # from native code, monocle oroutines return an object with a future that can be awaited:
    async def slow_fourth_power(x):
        y = await slow_square(x * x).future
        return y
