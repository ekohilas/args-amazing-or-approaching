<!-- intentionally blank -->

TODO: Update html for presenting

------

# PEP736 & Keyword Args: Kudos or Approaching? 
<!-- .element: class="r-fit-text" -->
### Evan Kohilas
### `@ekohilas` - `nohumanerrors.com`

Hello everyone!

As someone who's passionate about working towards nohumanerrors.com,

------

<div class="r-stack">
    <img src="images/hearts.png">
    <img src="images/python.svg">
</div>

I have utmost adoration for python's beautiful function argument system.

---
```python
def func(a, b):
    ...
```

Just look at it, isn't it great? Okay I'm not that crazy, ... at least I think.
Anyways, let's get some formalities out of the way. 

---
```python [2-3]
def func(
    a,
    b,
):
    ...
```

Anyone know what the name of these are called?

Anyone else thought they were called arguments?
Yeah it still confuses me...

---
```python [8-9]
def func(
    a,
    b,
):
    ...
    
func(
    a, 
    b, 
)
```

Okay so anyone want to take a guess at what these are called?

Anyone know what the name of these are?

Yeah these are arguments!

---
```python
def func(
    a,
    b,
):
    ...
    
func(
    a, 
    b, 
)
```

Okay now that that's out of the way let's go back to python's beautiful function argument system, that maybe I am crazy for...

---
```java
void rectangle(
    int width,
    int height,
);
```

I'll show this by example in comparison to most other languages. Here we have a function.

---
```java [6]
void rectangle(
    int width,
    int height,
);

basic_rectangle = rectangle(10, 20);
```
And we can call it to create a basic rectangle of a particular width and height.

```java
void rectangle(
    int width,
    int height,
);

basic_rectangle = rectangle(10, 20);
```
Now let's say that a basic rectangle isn't good enough, and we need to create a rotated one instead.

> TODO: Change type signature of rectangle

---
```java [4]
void rectangle(
    int width,
    int height,
    int rotation
);

basic_rectangle = rectangle(10, 20);
```

And to do so, we need to add the rotation paramter.

---
```java [7]
void rectangle(
    int width,
    int height,
    int rotation
);

basic_rectangle = rectangle(10, 20);
```
But now our previous function needs to be updated.

---
```java [7]
void rectangle(
    int width,
    int height,
    int rotation
);

basic_rectangle = rectangle(10, 20, 0);
```
And this creates a problem, because we now need to go through and update all existing function calls to specify a default rotation of 0.

```java
void rectangle(
    int width,
    int height,
    int rotation
);

basic_rectangle = rectangle(10, 20, 0);
```
But in most of these languages, there are other ways that a default rotation can be setup, so that this can be avoided.

------
```java
void rotated_rectangle(
    int width,
    int height,
    int rotation
);

void rectangle(
    int width,
    int height
) {
    rotated_rectangle(width, height, 0);
}
```
> TODO: Split
> TODO: Too wordy
And that is by creating a new function `rotated_rectangle` with this rotation parameter, and updating the old `rectangle` function, such that it calls the new `rotated_rectangle` function while setting the new `rotation` parameter with a default argument, which in our case will be 0.

Now you can start to see how this might get a bit messy. The good news it, that this messyness can be avoided through the use of function overloading.

------
```java
void rectangle(
    int width,
    int height
) {
    rectangle(width, height, 0);
}
```
This is function overloading, and it removes the need for us to rename any functions, as these programming languages will determine which functions to call using the parameter types instead.

That being said, this can also become problematic, for reasons that will become more apparrant later.

> as you can have multiple indetically named functions that may all do different things. Calling with the wrong arguments that have the same type but different names


------
```python [4]
def rectangle(
    width,
    height,
):
    ...

normal = rectangle(width, height)
```

So now if we switch back to Python,
So how does Python do it?

------
```python [4]
def rectangle(
    width,
    height,
    rotation=0,
):
    ...

normal = rectangle(width, height)
rotated = rectangle(width, height, rotation)
```

Well in python, since the concept of default arguments is built into the lanaguage (using the equals sign in the parameter definition)

------
```python [8-9]
def rectangle(
    width,
    height,
    rotation=0,
):
    ...

normal = rectangle(width, height)
rotated = rectangle(width, height, rotation)
```

there's no need for chained overloads, because if we don't specify a rotation, we've told it default to 0 instead.

------
```python
def rectangle(
    width,
    height,
    rotation=0,
):
    ...

normal = rectangle(width, height)
rotated = rectangle(width, height, rotation)
```

As a side note, Python is not perfect in this case either (I don't think any language is!)

And I highlight that because of one detail that can be easily missed.

------
```python
def rectangle(
    width,
    height,
    metadata={},
):
    ...
```

Let's say for example, that we wanted to set a default argument for our rectangles to contain metadata based on how they were created.

------
```python
def rectangle(
    width,
    height,
    metadata={},
):
    metadata["width"] = width
    metadata["height"] = height
```

And then, we added that metadata within the function.

------
```python
def rectangle(
    width,
    height,
    metadata={},
):
    metadata["width"] = width
    metadata["height"] = height
    
small = rectangle(10, 20)
big = rectangle(200, 100)
print(small.metadata) # {"width": 10, "height": 20"}
print(big.metadata)   # {"width": 200, "height": 100"}
```

What you'll find, is that instead of the obvious answer that you'd expect when printing this metadata

------
```python [11-12]
def rectangle(
    width,
    height,
    metadata={},
):
    metadata["width"] = width
    metadata["height"] = height
    
small = rectangle(10, 20)
big = rectangle(200, 100)
print(small.metadata) # {"width": 200, "height": 100"}
print(big.metadata)   # {"width": 200, "height": 100"}
```

Instead, their metadata is the same.

That's because these default parameters are instantiated at the time the function is defined, instead of when the function is called.

Giving this strange outcome, where all functions are sharing the same state.

------
```python [8-9]
def rectangle(
    width,
    height,
    rotation=0,
):
    ...

normal = rectangle(width, height)
rotated = rectangle(width, height, rotation)
```

Now if we step back to our original example, those of you that are experienced might be thinking of another way of how default arguments are usually done. 
> TODO: Code example
> TODO: Link all code
> TODO: Finalise code examples
> TODO: Add highlighting to code examples 
> TODO: Add code example replacing width/height with param1, param2, arg1, arg2

---
```java
Rectangle.builder(height, width)
    .build();
 
```
<!-- .element: data-notrim -->

And that is through a programming construct called the builder pattern, which stores and create this state.

---
```java
Rectangle.builder(height, width)
    .withRotation(rotation)
    .build();
```

This resolves this issue by allowing for optionally added data.

------
```java
Rectangle.builder(height, width)
    .build();
 
```
<!-- .element: data-notrim -->

But yet another issue lies, due to the nature of these **required** ordered arguments.
And that is that there's no knowing whether the arguments are set correctly 

------
<!-- .element: data-auto-animate -->
```java
Rectangle.builder(height, width)
    .build();
  
```
<!-- .element: data-notrim -->
<!-- .element: data-id="builder" -->

For example, put your hand up, if you noticed, that when I defined this builder, the ordering of height and width were swapped?

(Pause to look)

Even with [so many] people in this audience, there's actually only [a few] of you that realised that it should be width and height,

------
<!-- .element: data-auto-animate -->
```java [1,5,6]
Rectangle.builder(height, width)
    .build();
 
void rectangle(
    int width,
    int height
);
```
<!-- .element: data-id="builder" -->

Not height and width.
(3s pause for effect)

---
> TODO: add code

Going one step further, this same issue is what can cause function overloading to be harmful

Both of these are valid definitions, but updating an existing function to use rotation would lead to incorrect output.

rectangle(width, height, rotation)
vs
rectangle(height, width)


---
```python
rectangle(
    width=width,
    height=height,
)
```

Python is beautiful, in that it solves both of these issues with keyword arguments (and thus does away with builders and function overloading)

------
```python
rectangle(
    width=1,
    height=2,
)
```

Meaning that not only are our functions self documenting by having constant arguments labelled

------
```python
rectangle(
    height=2,
    width=1,
)
```

But now our argument ordering is redundant!

------
```python
rectangle(
    width=width,
    height=height,
)
```

Thus, by always using keyword arguments, our code is always future proofed against errors,

---
<!-- .element: data-auto-animate -->
```python []
def rectangle(
    height,
    width,
    rotation=0,
):
    ...

    
rectangle(1, 2, 3,)
```
<!-- .element: data-id="rectangle" -->

Like for example, if we go back to a default argument being used for rotation

------
<!-- .element: data-auto-animate -->
```python [9-13]
def rectangle(
    height,
    width,
    rotation=0,
):
    ...

    
rectangle(
    1,
    2,
    3,
)
```
<!-- .element: data-id="rectangle" -->

then we could call that function,

------
```python [12]
def rectangle(
    height,
    width,
    rotation=0,
):
    ...

    
rectangle(
    1, # height
    2, # width
    3, # rotation
)
```

with the 3rd argument overriding that default.

------
```python [4]
def rectangle(
    height,
    width,
    opacity,
    rotation=0,
):
    ...
    
rectangle(
    1,
    2,
    3,
)
```

But once we introduce a new required positional argument like opacity

------
```python [9-13]
def rectangle(
    height,
    width,
    opacity,
    rotation=0,
):
    ...
    
rectangle(
    1, # height
    2, # width
    3, # rotation
)
```

where 1, 2, and 3 were previously for height, width, and rotation

------
```python [12]
def rectangle(
    height,
    width,
    opacity,
    rotation=0,
):
    ...
    
rectangle(
    1, # height
    2, # width
    3, # opacity
)
```

They're now actually for height, width, and opacity, without us ever knowing.

------
```python [10-12]
def rectangle(
    height,
    width,
    opacity,
    rotation=0,
):
    ...
    
rectangle(
    height=1,
    width=2,
    opacity=3,
)
```

Naming our arguments easily lets us prevent this issue!

---
```python []
def rectangle(
    height,
    width,
    opacity,
    rotation=0,
):
    ...
    
rectangle(
    height=1,
    width=2,
    opacity=3,
)
```

But in addition, also reduces issues with refactoring!

------
```python [2-3]
def rectangle(
    width,
    height,
    opacity,
    rotation=0,
):
    ... 
    
rectangle(
    height=1,
    width=2,
    opacity=3,
)
```

such as in the case where we want to fix the mis-ordered parameters,

------
```python [10-11]
def rectangle(
    width,
    height,
    opacity,
    rotation=0,
):
    ...
    
rectangle(
    height=1,
    width=2,
    opacity=3,
)
```

we now don't have to make changes to re-order those arguments where that function is called.

---

Even if you're not refactoring, not using keyword arguments has led to errors.

```python
re.sub(pattern, repl, string, count=0, flags=0)
```
See if you can spot it in this example (and if you already know then let others have a guess)
>  https://github.com/python/cpython/issues/56166

---

Yes, Flags.MULTILINE isn't being passed in as a flag here, but instead as a count

and ... is an enum with value 0

so you can guess how many hours I spent trying to figure out why my regex substitution wasn't working, and second guessing my substitution function instead.

The way that Python is fixing this was by introducing a deprecation warning in python 3.13, noting that the use of count and flags as a positional argument will be removed and needs to be keyword instead.

And the way that they will do that is to put `*` as a parameter before those parameters

which will throw us an error when we try to call the function without naming those arguments.

Of course, if you're convinced by keyword arguments, you could force using them everywhere by putting * as the first paramters
but that can be tedious.

> TODO: figure out if the above or below works better

---

<!-- .element: data-auto-animate -->
```python []
def rectangle(
    height,
    width,
):
    ...
    
rectangle(
    1, # height
    2, # width
)
```
<!-- .element: data-id="named" -->

If you are convinced by keyword arguments, then there is a way to force using them,

------
<!-- .element: data-auto-animate -->
```python [2]
def rectangle(
    *,
    height,
    width,
):
    ...
    
rectangle(
    1, # height
    2, # width
)
```
<!-- .element: data-id="named" -->

and that is by putting `*` as the first parameter,

------
<!-- .element: data-auto-animate -->
```python [13-]
def rectangle(
    *,
    height,
    width,
):
    ...
    
rectangle(
    1, # height
    2, # width
)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: rectangle() takes 0 positional arguments but 2 were given
```
<!-- .element: data-id="named" -->

which will throw us an error when we try to call the function without naming our arguments.

But that can be cumbersome, as it can be forgotten, can make the code noisy, and would also require updating all previous functions.

---
<!-- .element: data-auto-animate -->
```python [8-9]
def rectangle(
    height,
    width,
):
    ...
    
rectangle(
    height=height,
    width=width,
)
```
<!-- .element: data-id="named" -->

Not to mention the redundant case where the names of the variables being passed in are the same as the parameters.

> TODO: Reference typescript or swift?

---
<!-- .element: data-auto-animate -->
```python [8-10]
def rectangle(
    height,
    width,
):
    ...
    
rectangle(
    # PEP736
    height=,
    width=,
)
```
<!-- .element: data-id="named" -->

The good news is, for when we don't have control over the interface, PEP736 is currently debating either using something like a trailing = for arguments that should take from variable names

------
<!-- .element: data-auto-animate -->
```python [8-10]
def rectangle(
    height,
    width,
):
    ...
    
rectangle(
    *, # PEP736
    height,
    width,
)
```
<!-- .element: data-id="named" -->

or adding `*` as an argument, for every argument afterwards to do the same.

------
<!-- .element: data-auto-animate -->
```python [8-9]
def rectangle(
    height,
    width,
):
    ...
    
rectangle(
    height,
    width,
)
```
<!-- .element: data-id="named" -->

Personally I feel like the best approach is for this sugar to be enabled and checked by default,

------
<!-- .element: data-auto-animate -->

```python [2, 9-10]
def rectangle(
    *,
    height,
    width,
):
    ...
    
rectangle(
    height,
    width,
)
```
<!-- .element: data-id="named" -->

or at the least, have `*` in the function definition specify that, that can be the case.

But given the way Python has been built, it might not be currently possible.

------
![ruff logo](images/ruff.svg)

So until something changes, I personally feel that linters are a cleaner, more pragmatic way to not only check, but also correct this for us!

---
<!-- .element: data-background-image="images/sprints.svg"-->

> TOOD: Update image to repo
> TODO: Could expand? e.g. this is because these lint rules can analyse the definitions during the calls of functions

So if this excites you, come contribute on making this lint rule a reality!

------

Or, if I've influenced you enough to start using this paradigm in your code day to day, here are some things that may be worth noting. 

------
```python
range(
    start=0,
    stop=10
    skip=2
)   
```

For one, you may notice in your excitement to add the parameter names as keyword arguments to all your function calls...

------
```python
>>> range(start=0, stop=1, skip=2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: range() takes no keyword arguments

```

that not _all_ functions are happy with that.

------
This is because of another special parameter, unlike `*` which makes all further parameters keyword only, 


------
`/` prevents all previous parameters from being passed using keywords.

Given the wonders you've just seen with keyword arguments, you might be wondering, how is this helpful?

------
Well there's two cases that I've found

The first may be made apparant if we had to refactor our function and change the name of our paramters.

For example, we may want to change the specification, and be more specific that the rotation is in degrees, not radians.

If we updated the name of our parameter, any calls that pass in the `rotation` argument would now fail.

Thus, by enforcing that a parameter like rotation can only be passed in as a positional argument, this refactoring would no longer be a breaking change.

Or maybe we want to keep the external argument name the same, and change the internal parameter name within our function.

We could do this by setting this parameter to another name at the top of the function.

However this can become messy, and the reference to the original paramter is still kept.

This is another case where you could argue that Python isn't perfect.

------
> TODO: Add swift example

If we look at other languages like Swift, then this concept exists as argument labels and paramter names.

------
```python
def map(
    iterable: typing.Iterable,
    with function: typing.Callable,
) -> list:
    return [function(item) for item in iterable]
    
map(
    [1, 2, 3],
    with=float,
)
```

If Python learned from Swift, then we would be able to do something like this, which lets us specify both an 


------
```python [3,5,9]
def map(
    iterable: typing.Iterable,
    with function: typing.Callable,
) -> list:
    return [function(item) for item in iterable]
    
map(
    [1, 2, 3],
    with=float,
)
```

external name like `with` and an internal name like `function`.

Isn't that cool! So much more readable!

> TODO: Update examples

------
> TODO: Javascript logo

Another language where this exists is Javascript

------
```javascript
function f({a: b}) {
    console.log(b);
}

f({a: 1})
```
Where it looks something like this.

------
```javascript
f(
{a: 1}
)
```

For those unfamiliar with javascript, there's quite a bit going on here.

Normally we have a function that takes in a single argument, which in our case is this thing in brackets that defines an object, similar to python's dictionaries

------
```javascript
function f(args) {
    const a = args.a
    console.log(b);
}

f({a: 1})
```

then that value can be assigned to a constant, such as a

------
```javascript
function f(args) {
    const {a} = args;
        const b = args.c;
    console.log(b);
}

f({a: 1})
```

but because of a language feature called object destructuring, we can have it assigned like this instead 

------
```javascript
function f(args) {
    const {a, b: c} = args;
    console.log(b);
}

f({a: 1})
```

we can also re-assign variables during descructuring

------
```javascript
function f({a, b: c}) {
    console.log(a);
}

f({a: 1})
```

And, because this feature works within the parameters of a function definition, we can do this!

And so javascript works similarly to swift, allowing us to rename our function parameters, and have different internal and external parameters names.

------
And additionally since this parameter is an object, it can be saved to a variable and only have that passed in instead.

------

Python let's you do this with dictionaries too!

------

By using the `**` operator within a function call, python will unpack the keys of the dictionary as the keywords, and the values as the arguments.

------

This might make you wonder, what happens if extra properties are passed into these function calls?

Well, I'm sorry to dissapoint you, but in javascript, the answer is, nothing. They don't get unpacked and thus they're ignored.

Buut, there is a way to keep them, and that is by using the `...rest` property.

Allowing us to save the remaining properties for whatever they may be needed for.

But if this is how javascript named parameters work, what happens in python, if we pass extra keyword arguments into a python function?

Well, unlike javascript, we'll get an error, telling us off that we passed in an unexpected keyword argument, which you could argue is pretty good default behaviour!

And I say default here because you can also specify a way to keep these leftover argumnets, and that is by using our good friend `**` again, adding it to a `rest` paramter.

As a side note, similar to javascript, this paramter doesn't have to be called `rest` either. The general convention in Python is `kwargs` for keyword args.

And unlike Javascript, Python currently doesn't have a way to unpack paramters within function definitions.

But fun fact, it did used to in python 2! https://peps.python.org/pep-3113/

Well... it was only for tuples

```python
>>> tuple = (1, 2)
>>> def func((a, b)):
...     print "a:", a, "b:", b
... 
>>> func(tuple)
a: 1 b: 2
```

But who knows, maybe it'll come back to Python after a PEP?

Anyways where were we...

So, by specifying `**kwargs` as the last parameter, any additional arguments that were passed in as keywords, and not caught by previous parameters will now be caught by `kwargs`.

What do I mean by this?

Remember how I mentioned earlier that there was two cases where you might want a `/` in your parameters?

Well, the second case is where you have a definition like this, both with a normal paramter and `**kwargs`.

And when you call this function with only keyword paramters, that first argument would be captured by the first paramter.

If you instead wanted this keyword argument to be captured by **kwargs, you can use the `/` operator to specify that that argument (along with all before it) is positional only.

Now you might have noticed that **kwargs is pretty cool, since it lets us pass in an arbitatry number of arguments.

But there are also cases where we can't define a keyword for every argument.

Say for example, when we want to sum a list of numbers.

This is where `*args` comes in, which is like **kwargs but for positional arguments.

`args` then appears as a variable that holds a tuple of all the arguments.

And similar to `**` within a function call, `*` can be used to unpack a list into these variable arguments.

Which is nesscary since if we want to pass arguments along, we can't use named arguments like args=args, or kwargs=kwargs.

It's also worth noting that by nature of `*args` capturing all additional positional arguments, any further paramters become keyword only.

`*` can also be used by itself, similar to `/`, if you still want to mandate that futher parameters are keyword only, but didn't want to capture additional positional arguments.

And there are good reasons for not wanting arbitrary keyword or positional arguments!

------
```rust
fn main() {
    println!("Hello", "world!");
}

//error: argument never used
// --> src/main.rs:2:23
//  |
//2 |     println!("Hello", "world!");
//  |              -------  ^^^^^^^^ argument never used
//  |              |
//  |              formatting specifier missing
```

For example, Rust doesn't support variable function arguments by design, as it hasn't found a way that wouldn't add complexity for the reader and the type checker to try and . Instead it encourages using macros which let the user encode the complexity or passing in lists which doesn't cause variable type signatures.

```python
f(*args, **kwargs):
```

And in Python, they can make functions difficult to understand how they should be used, given there's no need for types.

------
```python
f(*args: int, **kwargs: str):
```
Even if they are typed like this, then all the values need to be of the same type.

Which for the case of args is fine, because if they needed to be typed differently

------
```python
f(a1: int, a2: str, *args: int):
```
then in most cases, the definition should be updated with those param types.

> https://docs.python.org/3/library/typing.html#typing.TypeVarTuple

------
```python
from typing import TypedDict, Unpack

class Movie(TypedDict):
    name: str
    year: int

# This function expects two keyword arguments - `name` of type `str`
# and `year` of type `int`.
def foo(**kwargs: Unpack[Movie]): ...
```

And for typing keyword arguments, only from Python 3.11 were additions added as support.

> https://docs.python.org/3/library/typing.html#typing.Unpack
> https://typing.python.org/en/latest/spec/callables.html#unpack-kwargs
> https://chatgpt.com/share/67ea8fb7-5874-8004-a270-1fa956b296f2 

> If you're new to python, I will note for you to look into the other types of unpacking uses for this `*` operator, as that's outside the scope of this talk.
> TODO: Could cut this ** and * content. How to segue?

---

> TODO: Maybe use sub as the example isntead of rectangle to make the statement?

------
```python
def f(
    positional_only: int,
    positional_with_default: str = "hello",
    /,
    *aribitrary_argument_list: int,
    keyword_only_arg: str,
    **kwargs: typing.Unpack[Kw]
):
```
So to recap

This, is python's argument system

> TODO: run through them

and while You can argue that it's both approaching, and amazing
it's forever changing.

------

# <br> 
![pep736.nohumanerrors.com](images/pep736.nohumanerrors.com_qrcode.svg)<!-- .element: style="max-height: 95%"-->
<!-- .element: class="r-stretch"-->
# `pep736.nohumanerrors.com`
# `@ekohilas`

Or if you can't make it, you can find me online at @ekohilas, or collaborate with me on nohumanerrors.com.

------

# Thanks! 
![pep736.nohumanerrors.com](images/pep736.nohumanerrors.com_qrcode.svg)<!-- .element: style="max-height: 95%"-->
<!-- .element: class="r-stretch"-->
# `pep736.nohumanerrors.com`
# `@ekohilas`

Thanks to Joshua and Chris for authoring the PEP, and to you for listening!


------

------
```python
f(*args: int, **kwargs: str):
```
If you wanted to type specific args,

------
```python
f(*args: *tuple[int, ...]):
```
first we expand the definition to use the tuple form
you could do thisWith args, it can be re-written Even if they are typed like this, then all the values need to be of the same type.


------
```python
def foo(*args: *tuple[int, str, int, *tuple[]): ...
```

With args, you **can** specify

