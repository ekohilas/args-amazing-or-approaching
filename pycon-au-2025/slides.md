<!-- intentionally blank -->

> TODO: Fix sectioning
> TODO: Ensure height and width are ordered where they're meant to be
> TODO: Ensure all slides are highlighting the right part
> TODO: Add void to function signatures
> TODO: Spellcheck final
> TODO: Check code is linked properly
> TODO: Check code examples
> TODO: Add history notes for when features were introduced

------

# Args: Amazing<br>or Approaching?
<!-- .element: class="r-fit-text" -->
## Evan Kohilas
## `@ekohilas` - `nohumanerrors.com`

Hello everyone!

Are you excited?!
Great! Because I am too since...

------

<div class="r-stack">
    <img src="images/hearts.png">
    <img src="images/python.svg">
</div>

I have utmost adoration for python's beautiful function argument and parameter system.

------
<!-- .element: data-auto-animate -->
```python []
def function(
    a,
    b,
):
    ...
```
<!-- .element: data-id="code" -->

Just look at it, isn't it great? Okay I'm not that crazy, ... at least I think.
Anyways, let's get some formalities out of the way.

------
<!-- .element: data-auto-animate -->
```python [2-3]
def function(
    a,
    b,
):
    ...
```
<!-- .element: data-id="function" -->

Anyone know what the name of these are called?

[Anyone else thought they were called arguments?]

[Yeah it still gets me, so don't fault me if I get confused!]

------
<!-- .element: data-auto-animate -->
```python [8-9]
def function(
    a,
    b,
):
    ...

function(
    a,
    b,
)
```
<!-- .element: data-id="function" -->

Okay so, anyone want to take a guess at what these are called?

Yeah these are arguments!

------
<!-- .element: data-auto-animate -->
```python []
def function(
    a,
    b,
):
    ...

function(
    a,
    b,
)
```
<!-- .element: data-id="function" -->

Okay now that that's out of the way let's go back to python's beautiful function argument and parameter system, that maybe I am crazy for...

------
<!-- .element: data-auto-animate -->
```java []
void function(
    int a,
    int b
) {
    // function code
}
```
<!-- .element: data-id="code" -->

To show what I mean, I'll start by using a function from another language.

------
```java []
Rectangle rectangle(
    int width,
    int height
) {
    // function code
}
```
<!-- .element: data-id="code" -->

And I'll change it up to a more concrete,

------
<!-- .element: data-auto-animate -->
```java []
Rectangle rectangle(
    int width,
    int height
) {
    // function code
}
```
<!-- .element: data-id="code" -->

relatable example, making rectangles!

------
<!-- .element: data-auto-animate -->
```java []
Rectangle rectangle(
    int width,
    int height
);
```
<!-- .element: data-id="code" -->

I'll also simplify it down to the function type signature.

------
<!-- .element: data-auto-animate -->
```java [6]
Rectangle rectangle(
    int width,
    int height
);

basic = rectangle(10, 20);
```
<!-- .element: data-id="code" -->

And now, this function can be called to create a basic rectangle of a particular width and height.

------
<!-- .element: data-auto-animate -->
```java []
Rectangle rectangle(
    int width,
    int height
);

basic = rectangle(10, 20);
```
<!-- .element: data-id="code" -->

But let's say that a basic rectangle isn't good enough. And we've been asked to create a rotated one instead.

> TODO: Change return type signature of rectangle

------
<!-- .element: data-auto-animate -->
```java [4]
Rectangle rectangle(
    int width,
    int height,
    int rotation
);

basic = rectangle(10, 20);
```
<!-- .element: data-id="code" -->

And to do so, we need to add the rotation parameter.

------
<!-- .element: data-auto-animate -->
```java [8]
Rectangle rectangle(
    int width,
    int height,
    int rotation
);

basic = rectangle(10, 20);
rotated = rectangle(10, 20, 45);
```
<!-- .element: data-id="code" -->

Now we can make a rotated rectangle!

------
<!-- .element: data-auto-animate -->
```java [6-8]
Rectangle rectangle(
    int width,
    int height,
    int rotation
);
basic = rectangle(10, 20); 
// error: constructor Rectangle in class Rectangle
//          cannot be applied to given types;
rotated = rectangle(10, 20, 45);
```
<!-- .element: data-id="code" -->

But now our previous function call needs to be updated, as it'll now error from not enough arguments.

------
<!-- .element: data-auto-animate -->
```java [7]
Rectangle rectangle(
    int width,
    int height,
    int rotation
);

basic = rectangle(10, 20, 0);
rotated = rectangle(10, 20, 45);
```
<!-- .element: data-id="code" -->

And this creates a problem, because we now need to go through and update all existing function calls for any un-rotated rectangles, and add an additional argument for a default rotation of 0

------
<!-- .element: data-auto-animate -->
```java []
Rectangle rectangle(
    int width,
    int height,
    int rotation
);

basic = rectangle(10, 20, 0);
rotated = rectangle(10, 20, 45);
```
<!-- .element: data-id="code" -->

Because this is tedious work that we want to avoid, in most of these languages, there are other ways that a default rotation can be setup.

------
<!-- .element: data-auto-animate -->
```java [1,4]
Rectangle rotated_rectangle(
    int width,
    int height,
    int rotation
);

Rectangle rectangle(
    int width,
    int height
);

basic = rectangle(10, 20);
rotated = rotated_rectangle(10, 20, 45);
```
<!-- .element: data-id="code" -->

The most basic way, is by creating a new function with this rotation parameter.

Of course, we don't want to duplicate the code that makes these rectangles.

------
<!-- .element: data-auto-animate -->
```java [10-12]
Rectangle rotated_rectangle(
    int width,
    int height,
    int rotation
);

Rectangle rectangle(
    int width,
    int height
) {
    return rotated_rectangle(width, height);
}

basic = rectangle(10, 20);
rotated = rotated_rectangle(10, 20, 45);
```
<!-- .element: data-id="code" -->

So we update the old function, such that it calls the new function

------
```java [10-12]
Rectangle rotated_rectangle(
    int width,
    int height,
    int rotation
);

Rectangle rectangle(
    int width,
    int height
) {
    return rotated_rectangle(width, height, 0);
}

basic = rectangle(10, 20);
rotated = rotated_rectangle(10, 20, 45);
```
<!-- .element: data-id="code" -->

And sets the new parameter with a default argument, which in our case will be 0.

------
<!-- .element: data-auto-animate -->
```java []
Rectangle rotated_rectangle(
    int width,
    int height,
    int rotation
);

Rectangle rectangle(
    int width,
    int height
) {
    return rotated_rectangle(width, height, 0);
}

basic = rectangle(10, 20);
rotated = rotated_rectangle(10, 20, 45);
```
<!-- .element: data-id="code" -->

Now if we take a step back, we might start to see how this might get a bit messy. The good news is, in some languages, we can do a bit of clean up through the use of function overloading.

------
<!-- .element: data-auto-animate -->
```java [1-4,7-9]
Rectangle rectangle(
    int width,
    int height,
    int rotation
);

Rectangle rectangle(
    int width,
    int height
) {
    return rectangle(width, height, 0);
}

basic = rectangle(10, 20);
rotated = rectangle(10, 20, 45);
```
<!-- .element: data-id="code" -->

With function overloading, we can define multiple functions with the same name, but different type signatures.

> TODO: Split into two slides (one on names, another on type signatures)

------
<!-- .element: data-auto-animate -->
```java [11,14,15]
Rectangle rectangle(
    int width,
    int height,
    int rotation
);

Rectangle rectangle(
    int width,
    int height
) {
    return rectangle(width, height, 0);
}

basic = rectangle(10, 20);
rotated = rectangle(10, 20, 45);
```
<!-- .element: data-id="code" -->

This removes the need for us to rename any functions, as these programming languages will determine which functions to call using the parameter types instead.

------
<!-- .element: data-auto-animate -->
```python []
def rectangle(
    width,
    height,
    rotation,
): ...

def rectangle(
    width,
    height,
):
    return rectangle(width, height, 0)

basic = rectangle(10, 20)
rotated = rectangle(10, 20, 45)
```
<!-- .element: data-id="code" -->

If we looked at the same code in python

------
<!-- .element: data-auto-animate -->
```python [14-16]
def rectangle(
    width,
    height,
    rotation,
): ...

def rectangle(
    width,
    height,
):
    return rectangle(width, height, 0)

basic = rectangle(10, 20)
rotated = rectangle(10, 20, 45)
# TypeError: rectangle() takes 2 positional arguments
#              but 3 were given
```
<!-- .element: data-id="code" -->

It would fail!

> TODO: fix failure to appear on slide

------
<!-- .element: data-auto-animate -->
```python [1,7]
def rectangle(
    width,
    height,
    rotation,
): ...

def rectangle(
    width,
    height,
):
    return rectangle(width, height, 0)

basic = rectangle(10, 20)
rotated = rectangle(10, 20, 45)
```
<!-- .element: data-id="code" -->

And this is because in Python, defining a function with the same name overwrites the previous definition.

------
<!-- .slide: data-background-image="images/multipledispatch-pypi.png"-->

While there are packages like multipledispatch that you can use to replicate function overloading

------
<!-- .slide: data-background-image="images/overloading-problem.png"-->

function overloading in general can also become problematic, for reasons that will become more apparent later.

------
<!-- .element: data-auto-animate -->
```python []
def rotated_rectangle(
    width,
    height,
    rotation,
): ...

def rectangle(
    width,
    height,
):
    return rotated_rectangle(width, height, 0)

basic = rectangle(10, 20)
rotated = rotated_rectangle(10, 20, 45)
```
<!-- .element: data-id="code" -->

So without function overloading, how does Python let us simplify this?

------
<!-- .element: data-auto-animate -->
```python [4]
def rotated_rectangle(
    width,
    height,
    rotation=0,
): ...

def rectangle(
    width,
    height,
):
    return rotated_rectangle(width, height, 0)

basic = rectangle(10, 20)
rotated = rotated_rectangle(10, 20, 45)
```
<!-- .element: data-id="code" -->

Well in python, the concept of default arguments is built into the language (using the equals sign in the parameter definition)

------
<!-- .element: data-auto-animate -->
```python [7]
def rotated_rectangle(
    width,
    height,
    rotation=0,
): ...

basic = rotated_rectangle(10, 20, 0)
rotated = rotated_rectangle(10, 20, 45)
```
<!-- .element: data-id="code" -->

So now, if we only keep a single definition, we can remove the need for function chaining

------
<!-- .element: data-auto-animate -->
```python [7]
def rotated_rectangle(
    width,
    height,
    rotation=0,
): ...

basic = rotated_rectangle(10, 20)
rotated = rotated_rectangle(10, 20, 45)
```
<!-- .element: data-id="code" -->

And then, remove the need to pass in 0, since it'll use the default instead.

------
<!-- .element: data-auto-animate -->
```python [1,7,8]
def rectangle(
    width,
    height,
    rotation=0,
): ...

basic = rectangle(10, 20)
rotated = rectangle(10, 20, 45)
```
<!-- .element: data-id="code" -->

Then we can rename our function back to rectangle, to get our beautiful definition.

------
<!-- .slide: data-background-image="images/sunshine_and_rainbows.svg"-->

As a side note, Python is not all sunshine and rainbows either (I don't think any language is!)

And I highlight that because of one detail that can be easily missed.

------
<!-- .element: data-auto-animate -->
```python [4]
def rectangle(
    width,
    height,
    metadata={},
):
    ...
```
<!-- .element: data-id="code" -->

Let's say for example, that we wanted to set a default argument for our rectangles to contain metadata based on how they were created.

------
<!-- .element: data-auto-animate -->
```python [6-7]
def rectangle(
    width,
    height,
    metadata={},
):
    metadata["width"] = width
    metadata["height"] = height
```
<!-- .element: data-id="code" -->

And then, we added that metadata within the function.

------
<!-- .element: data-auto-animate -->
```python [12-13]
def rectangle(
    width,
    height,
    metadata={},
):
    metadata["width"] = width
    metadata["height"] = height

small = rectangle(10, 20)
big = rectangle(300, 400)

print(small.metadata) # {"width": 10, "height": 20"}
print(big.metadata)   # {"width": 300, "height": 400"}
```
<!-- .element: data-id="code" -->

What you'll find, is that instead of the obvious answer that you'd expect when printing this metadata

------
<!-- .element: data-auto-animate -->
```python [12-13]
def rectangle(
    width,
    height,
    metadata={},
):
    metadata["width"] = width
    metadata["height"] = height

small = rectangle(10, 20)
big = rectangle(300, 400)

print(small.metadata) # {"width": 300, "height": 400"}
print(big.metadata)   # {"width": 300, "height": 400"}
```
<!-- .element: data-id="code" -->

Instead, their metadata ends up being the same.

------
<!-- .element: data-auto-animate -->
```python [4]
def rectangle(
    width,
    height,
    metadata={},
):
    metadata["width"] = width
    metadata["height"] = height

small = rectangle(10, 20)
big = rectangle(300, 400)

print(small.metadata) # {"width": 300, "height": 400"}
print(big.metadata)   # {"width": 300, "height": 400"}
```
<!-- .element: data-id="code" -->

This is because in Python, the values for these default parameters are created when the function is defined, **not** when it's called.

------
<!-- .element: data-auto-animate -->
```python [12-13]
def rectangle(
    width,
    height,
    metadata={},
):
    metadata["width"] = width
    metadata["height"] = height

small = rectangle(10, 20)
big = rectangle(300, 400)

print(small.metadata) # {"width": 300, "height": 400"}
print(big.metadata)   # {"width": 300, "height": 400"}
```
<!-- .element: data-id="code" -->

Giving this strange outcome, where all functions are sharing the same state.

------
<!-- .element: data-auto-animate -->
```python [4,6-7]
def rectangle(
    width,
    height,
    metadata=None,
):
    if metadata is None:
        metadata = {}

    metadata["width"] = width
    metadata["height"] = height

small = rectangle(10, 20)
big = rectangle(300, 400)

print(small.metadata) # {"width": 10, "height": 20"}
print(big.metadata)   # {"width": 300, "height": 400"}
```
<!-- .element: data-id="code" -->

So if your functions need mutable defaults, the best way to do so is to default them to None, and set the mutable that you want if it hasn't been specified.

> TODO: Update example to use 3/4 not 1/2

------
<!-- .slide: data-background-image="images/thunderstorms_and_lightning.svg"-->

Now if we step away from the thunderstorms and lightning (which are very very frightening),

------
<!-- .element: data-auto-animate -->
```java []
Rectangle rectangle(
    int width,
    int height
);

basic = rectangle(10, 20);
```
<!-- .element: data-id="code" -->

and go back to our original non python example,

------
<!-- .element: data-auto-animate -->
```java []
Rectangle rectangle(
    int width,
    int height
    /* int rotation=0 how? */
);

basic = rectangle(10, 20);
```
<!-- .element: data-id="code" -->

how could defaults be done in a language that doesn't support them?

------
<!-- .element: data-auto-animate -->
```java []
var rectangle = Rectangle
    .builder(height, width)
    .build();

```
<!-- .element: data-notrim -->
<!-- .element: data-id="builder" -->

Well, some of you might be familiar with a programming construct called the builder pattern.

------
<!-- .element: data-auto-animate -->
```java [2]
var rectangle = Rectangle
    .builder(height, width)
    .build();

```
<!-- .element: data-notrim -->
<!-- .element: data-id="builder" -->

On initiation, it requires and stores all necessary data

------
<!-- .element: data-auto-animate -->
```java [3]
var rectangle = Rectangle
    .builder(height, width)
    .withRotation(rotation)
    .build();
```
<!-- .element: data-notrim -->
<!-- .element: data-id="builder" -->

and then allows for adding of any optional data

------
<!-- .element: data-auto-animate -->
```java [4]
var rectangle = Rectangle
    .builder(height, width)
    .withRotation(rotation)
    .build();
```
<!-- .element: data-notrim -->
<!-- .element: data-id="builder" -->

before building the final state.

------
<!-- .element: data-auto-animate -->
```java []
var rectangle = Rectangle
    .builder(height, width)
    .build();

```
<!-- .element: data-notrim -->
<!-- .element: data-id="builder" -->

But yet another issue lies with required arguments, that even builders can't fix.

Can anyone spot the error here?

(water break)

------
<!-- .element: data-auto-animate -->
```java [2]
var rectangle = Rectangle
    .builder(height, width)
    .build();

```
<!-- .element: data-notrim -->
<!-- .element: data-id="builder" -->

[No one noticed, that when I defined this builder, the ordering of height and width were swapped?]

[Yes well done] It should be width and height,

------
<!-- .element: data-auto-animate -->
```java [2,6-7]
var rectangle = Rectangle
    .builder(height, width)
    .build();

Rectangle rectangle(
    int width,
    int height
);
```
<!-- .element: data-id="builder" -->

Not height and width.

(pause for effect)

And, in case you were wondering, I _have_ seen this in a codebase.

------
<!-- .element: data-auto-animate -->
```java [1,6,12,13]
Rectangle rectangle(
    int width,
    int height
);

Rectangle rectangle(
    int height,
    int width,
    int rotation
);

shape_1 = rectangle(10, 20);
shape_2 = rectangle(20, 10, 45);
```
<!-- .element: data-notrim -->
<!-- .element: data-id="builder" -->

Going one step further, this same issue is what can cause function overloading to be harmful.

For example, both of these are valid definitions,

------
<!-- .element: data-auto-animate -->
```java [2-3,7-8]
Rectangle rectangle(
    int width,
    int height
);

Rectangle rectangle(
    int height,
    int width,
    int rotation
);

shape_1 = rectangle(10, 20);
shape_2 = rectangle(20, 10, 45);
```
<!-- .element: data-notrim -->
<!-- .element: data-id="builder" -->

the only difference being the ordering of the parameters

------
<!-- .element: data-auto-animate -->
```java [13]
Rectangle rectangle(
    int width,
    int height
);

Rectangle rectangle(
    int height,
    int width,
    int rotation
);

shape_1 = rectangle(10, 20);
shape_2 = rectangle(20, 10);
```
<!-- .element: data-notrim -->
<!-- .element: data-id="builder" -->

But as soon as we remove the rotation of the shape, the shapes dimensions are now different.

------
<!-- .element: data-auto-animate -->
```java [2-3,7-8]
Rectangle rectangle(
    int width,
    int height
);

Rectangle rectangle(
    int height,
    int width,
    int rotation
);

shape_1 = rectangle(10, 20);
shape_2 = rectangle(20, 10);
```
<!-- .element: data-notrim -->
<!-- .element: data-id="builder" -->

Without having to reference the signature of the functions, there's no knowing whether the arguments are set correctly.

------
<!-- .element: data-auto-animate -->
```python []
rectangle(
    width=width,
    height=height,
)
```
<!-- .element: data-id="code" -->

Python is beautiful, in that it solves both of these issues with keyword arguments (and thus does away with builders and function overloading)

------
<!-- .element: data-auto-animate -->
```python []
rectangle(
    width=10,
    height=20,
)
```
<!-- .element: data-id="code" -->

Meaning that not only are our functions self documenting by having constant arguments labelled
> TODO: fix numbering of arguments above

------
<!-- .element: data-auto-animate -->
```python []
rectangle(
    height=20,
    width=10,
)
```
<!-- .element: data-id="code" -->

But now our argument ordering is redundant!

------
<!-- .slide: data-background-image="images/never_ending_benefits.svg"-->

This might not seem like much, but this little change, of always using keywords arguments, leads to so many benefits, and prevention of errors.

------
<!-- .element: data-auto-animate -->
```python [4]
def rectangle(
    height,
    width,
    rotation=0,
):
    ...

rectangle(
    10, # height
    20, # width
    45, # rotation
)
```
<!-- .element: data-id="rectangle" -->

Like for example, if we go back to a default argument being used for rotation

------
<!-- .element: data-auto-animate -->
```python [8-12]
def rectangle(
    height,
    width,
    rotation=0,
):
    ...

rectangle(
    10, # height
    20, # width
    45, # rotation
)
```
<!-- .element: data-id="code" -->

then we could call that function,

------
<!-- .element: data-auto-animate -->
```python [11]
def rectangle(
    height,
    width,
    rotation=0,
):
    ...

rectangle(
    10, # height
    20, # width
    45, # rotation
)
```
<!-- .element: data-id="code" -->

with the 3rd argument overriding that default.

------
<!-- .element: data-auto-animate -->
```python [4]
def rectangle(
    height,
    width,
    opacity,
    rotation=0,
):
    ...

rectangle(
    10, # height
    20, # width
    45, # rotation
)
```
<!-- .element: data-id="code" -->

But once we introduce a new required positional argument like opacity

------
<!-- .element: data-auto-animate -->
```python [9-13]
def rectangle(
    height,
    width,
    opacity,
    rotation=0,
):
    ...

rectangle(
    10, # height
    20, # width
    45, # rotation
)
```
<!-- .element: data-id="code" -->

where 10, 20, and 45 were previously for height, width, and rotation

------
<!-- .element: data-auto-animate -->
```python [12]
def rectangle(
    height,
    width,
    opacity,
    rotation=0,
):
    ...

rectangle(
    10, # height
    20, # width
    45, # opacity
)
```
<!-- .element: data-id="code" -->

They're now actually for height, width, and opacity, without us ever knowing.

------
<!-- .element: data-auto-animate -->
```python [10-12]
def rectangle(
    height,
    width,
    opacity,
    rotation=0,
):
    ...

rectangle(
    height=10,
    width=20,
    opacity=45,
)
```
<!-- .element: data-id="code" -->

Naming our arguments easily lets us prevent this issue!

------
<!-- .element: data-auto-animate -->
```python []
def rectangle(
    height,
    width,
    opacity,
    rotation=0,
):
    ...

rectangle(
    height=10,
    width=20,
    opacity=45,
)
```
<!-- .element: data-id="code" -->

But in addition, also reduces issues with refactoring!

------
<!-- .element: data-auto-animate -->
```python [2-3]
def rectangle(
    width,
    height,
    opacity,
    rotation=0,
):
    ...

rectangle(
    height=10,
    width=20,
    opacity=45,
)
```
<!-- .element: data-id="code" -->

such as in the case where we want to fix the mis-ordered parameters,

------
<!-- .element: data-auto-animate -->
```python [10-11]
def rectangle(
    width,
    height,
    opacity,
    rotation=0,
):
    ...

rectangle(
    height=10,
    width=20,
    opacity=45,
)
```
<!-- .element: data-id="code" -->

we now don't have to make changes to re-order those arguments everywhere that function is called.

------
<!-- .element: data-auto-animate -->
```python [2-3,8-9]
def rectangle(
    height,
    width,
):
    ...

rectangle(
    height=10,
    width=20,
)
```
<!-- .element: data-id="code" -->

And if we choose to sort the ordering of arguments and parameters, we can reduce the chance of merge conflicts

------
<!-- .element: data-auto-animate -->
```python [3-4,11-12]
def rectangle(
    height,
    opacity,
    rotation,
    width,
):
    ...

rectangle(
    height=10,
    opacity=30,
    rotation=45,
    width=20,
)
```
<!-- .element: data-id="code" -->

for example, if one commit adds opacity and rotation,

------
<!-- .element: data-auto-animate -->
```python [2,4,10,12]
def rectangle(
    color,
    height,
    opacity,
    width,
):
    ...

rectangle(
    color="green"
    height=10,
    opacity=30,
    width=20,
)
```
<!-- .element: data-id="code" -->

and the other adds opacity and color, as when they're combined

------
<!-- .element: data-auto-animate -->
```python [2,4,5,11,13,14]
def rectangle(
    color,
    height,
    opacity,
    rotation,
    width,
):
    ...

rectangle(
    color="green"
    height=10,
    opacity=30,
    rotation=40,
    width=20,
)
```
<!-- .element: data-id="code" -->

opacity will be in the same place for both.

------
<!-- .slide: data-background-image="images/no_teamwork.svg"-->

Even if you don't care for refactoring or collaboration, I'd still recommend using keyword arguments to reduce human errors.

------
<!-- .element: data-auto-animate -->
```python []
re.sub(
    r"(\w+)(\[.*?\])\s*\n(.*?)",
    replacement_function,
    content,
    re.IGNORECASE,
)
```
<!-- .element: data-id="code" -->

Pop quiz!
Can anyone spot the error in this example?
(and if you already know then let others have a chance)
(water break)
(hint, it's do to with function arguments and parameters)

> TODO: continue code and slide numbering from here

>  https://github.com/python/cpython/issues/56166

------
<!-- .element: data-auto-animate -->
```python [5]
re.sub(
    r"(\w+)(\[.*?\])\s*\n(.*?)",
    replacement_function,
    content,
    re.IGNORECASE,
)
```
<!-- .element: data-id="code" -->

[Yes!]

It's how the IGNORECASE flag is being passed in!

Side note: Isn't it interesting how much harder errors are to spot when there's complexity?

This is pretty hard to spot if we don't know the function definition, so let's bring it up.

------
<!-- .element: data-auto-animate -->
```python [8-14]
re.sub(
    r"(\w+)(\[.*?\])\s*\n(.*?)",
    replacement_function,
    content,
    re.IGNORECASE,
)

def sub(
    pattern,
    repl,
    string,
    count=0,
    flags=0,
)
```
<!-- .element: data-id="code" -->

If we look at the definition of re.sub,

------
<!-- .element: data-auto-animate -->
```python [5,12]
re.sub(
    r"(\w+)(\[.*?\])\s*\n(.*?)",
    replacement_function,
    content,
    re.IGNORECASE,
)

def sub(
    pattern,
    repl,
    string,
    count=0,
    flags=0,
)
```
<!-- .element: data-id="code" -->

and we look at the parameter that the flag is passed in as, you'll see it's count, not flags.

------
<!-- .element: data-auto-animate -->
```python [5]
re.sub(
    r"(\w+)(\[.*?\])\s*\n(.*?)",
    replacement_function,
    content,
    re.IGNORECASE, # 2
)

def sub(
    pattern,
    repl,
    string,
    count=0,
    flags=0,
)
```
<!-- .element: data-id="code" -->

and then the flag is read as an int, setting the maximum number of substitutions to 2.

That would explain why I spent hours trying to figure out why my expected thousands of substitutions weren't working, and was instead second guessing my replacement function.

------
<!-- .slide: data-background-image="images/positional-deprecated.png"-->

In fact, so many people have had this issue, that Python has fixed it by introducing a deprecation warning from 3.13, noting that the use of count and flags as a positional argument will be removed and needs to be a keyword instead.

------
<!-- .element: data-auto-animate -->
```python [5,13]
re.sub(
    r"(\w+)(\[.*?\])\s*\n(.*?)",
    replacement_function,
    content,
    flags=re.IGNORECASE,
)

def sub(
    pattern,
    repl,
    string,
    *,
    count=0,
    flags=0,
)
```
<!-- .element: data-id="code" -->

And the way that they will do that, is to put `*` as a parameter before count and flags.

> TODO: remove flags= and Fix highlighting to include * and count/flags

------
<!-- .element: data-auto-animate -->
```python []
re.sub(
    r"(\w+)(\[.*?\])\s*\n(.*?)",
    replacement_function,
    content,
    re.IGNORECASE,
)

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: sub() takes 3 positional arguments but 4 were given

```
<!-- .element: data-id="code" -->

What this will do, is throw us an error when we try to call the function without naming those arguments.

> TODO: add slide with flags having argument
> TOOD: clean up error

------
<!-- .element: data-auto-animate -->
```python []
def rectangle(
    height,
    width,
):
    ...

rectangle(
    10, # height
    20, # width
)
```
<!-- .element: data-id="named" -->

So, if you are convinced by keyword arguments, and want to ensure that functions like rectangle are always called with them.

------
<!-- .element: data-auto-animate -->
```python [2,9-10]
def rectangle(
    *,
    width,
    height,
):
    ...

rectangle(
    height=10,
    width=20,
)
```
<!-- .element: data-id="named" -->

then one way you could force that, is by putting `*` as the first parameter,

------
<!-- .slide: data-background-image="images/agonising-emoji.png"-->

But that can be cumbersome, as it can be forgotten, can make the code noisy, and would also require updating all previously made functions.

------
<!-- .element: data-auto-animate -->
```python [8-9]
def rectangle(
    width,
    height,
):
    ...

rectangle(
    height=height,
    width=width,
)
```
<!-- .element: data-id="named" -->

Not to mention the redundant cases where the names of the variables being passed in are the same as the parameters.
And while it might look fine in this case,

------
<!-- .element: data-auto-animate -->
```python []
rectangle(
    top_left_pos_from_x_origin=top_left_pos_from_x_origin,
    top_left_pos_from_y_origin=top_left_pos_from_x_origin,
    bottom_right_pos_from_x_origin=bottom_right_pos_from_x_origin,
    bottom_right_pos_from_y_origin=bottom_right_pos_from_y_origin,
    rotation_in_radians=rotation_in_radians,
    color_in_hex=color_in_hex,
    line_thickness_in_pixels=line_thickness_in_pixels,
)
```
<!-- .element: data-id="long" -->

it can get pretty unreadable when the number of parameters and their names are much longer...

For example, has anyone spotted the mistake here?

------
<!-- .element: data-auto-animate -->
```python [3]
rectangle(
    top_left_pos_from_x_origin=top_left_pos_from_x_origin,
    top_left_pos_from_y_origin=top_left_pos_from_x_origin,
    bottom_right_pos_from_x_origin=bottom_right_pos_from_x_origin,
    bottom_right_pos_from_y_origin=bottom_right_pos_from_y_origin,
    rotation_in_radians=rotation_in_radians,
    color_in_hex=color_in_hex,
    line_thickness_in_pixels=line_thickness_in_pixels,
)
```
<!-- .element: data-id="long" -->

Yeah it's in the 2nd argument, where the x should be a y.

------
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

The good news is, I'm not the only one who's thought about this.

PEP736 proposes using a trailing = for arguments that should take from existing variable names

------
<!-- .slide: data-background-image="images/pep_rejected.svg"-->

The bad news is, that this was rejected earlier this year...

------
![ruff logo](images/ruff.svg)

Personally I feel that linters are a cleaner, more pragmatic way to not only check, but also correct this for us!

------
<!-- .element: data-auto-animate -->
```python [2, 9-10]
def rectangle(
    *,
    width,
    height,
):
    ...

rectangle(
    height=height,
    width=width,
)
```
<!-- .element: data-id="code" -->

For example, a rule that enforces (and auto adds) a star on all function definitions.

------
<!-- .element: data-auto-animate -->
```python [2-3,8-9]
def rectangle(
    width,
    height,
):
    ...

rectangle(
    height=height,
    width=width,
)
```
<!-- .element: data-id="code" -->

Or if that's not up your alley, a rule that enforces all function calls to use keyword arguments wherever possible

------
<!-- .element: data-auto-animate -->
```python [3,9]
def rectangle(
    width,
    height,
):
    ...

rectangle(
    width,
    width,
)
```
<!-- .element: data-id="code" -->

Or, if you want the safety without the redundancy, a rule that for this parameter and argument,

------
<!-- .element: data-auto-animate -->
```python [3,9-10]
def rectangle(
    width,
    height,
):
    ...

rectangle(
    width,
    # "width" argument name != "height" parameter name.
    width,
)
```
<!-- .element: data-id="code" -->

Warns when a parameter and argument don't match.

------
<!-- .element: data-auto-animate -->
```python [3,9]
def rectangle(
    width,
    height,
):
    ...

rectangle(
    width,
    height=width,
)
```
<!-- .element: data-id="code" -->

And if that's the intention, provides a fix to bring clarity with a keyword argument.

------
<!-- .slide: data-background-image="images/github-logo.png"-->

So if mitigating human errors excites you, I'd love to talk with you on how we can make more of these kinds of tools!

> NOTE: Could expand? e.g. this is because these lint rules can analyse the definitions during the calls of functions

------
<!-- .slide: data-background-image="images/inspired-emoji.png"-->

Or, if I've inspired you enough to start using this paradigm in your code day to day, here are some things that may be worth noting.

------
<!-- .element: data-auto-animate -->
```python []
range(
    start=0,
    stop=10,
    skip=20,
)
```
<!-- .element: data-id="code" -->

For one, you may notice in your excitement to use keyword arguments for all your function calls...

------
<!-- .element: data-auto-animate -->
```python [6]
range(
    start=0,
    stop=10,
    skip=20,
)
# TypeError: range() takes no keyword arguments
```
<!-- .element: data-id="code" -->

that not _all_ functions are happy with that.

------
```python [5]
def range(
    start,
    stop,
    skip=10,
    /,
)
```
<!-- .element: data-id="code" -->

This is because of another special parameter, `/`.
Unlike `*` which makes all further parameters keyword only,
`/` prevents all previous parameters from being passed into using keyword arguments.

------
![but why gif](images/but_why.gif)

Given the wonders you've just seen with keyword arguments, you might be wondering, when is this helpful?

Well there's three cases that I've seen

------
<!-- .element: data-auto-animate -->
```python []
def rectangle(
    width,
    height,
    rotation=0,
):
    ...

rectangle(
    height=10,
    width=20,
    rotation=45,
)
```
<!-- .element: data-id="code" -->

The first may be made apparent if we had to refactor our function and change the name of our parameters.

------
<!-- .element: data-auto-animate -->
```python [4]
def rectangle(
    width,
    height,
    rotation_in_degrees=0,
):
    ...

rectangle(
    height=10,
    width=20,
    rotation=45,
)
```
<!-- .element: data-id="code" -->

For example, we may want to change the specification, and be more specific that the rotation is in degrees, not radians.

------
<!-- .element: data-auto-animate -->
```python [11,14-16]
def rectangle(
    width,
    height,
    rotation_in_degrees=0,
):
    ...

rectangle(
    height=10,
    width=20,
    rotation=45,
)

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: rectangle() got an unexpected keyword argument 'rotation'
```
<!-- .element: data-id="code" -->

If we updated the name of our parameter, now any calls that pass in the `rotation` argument would now fail.

------
<!-- .element: data-auto-animate -->
```python [5]
def rectangle(
    width,
    height,
    rotation_in_degrees=0,
    /,
):
    ...

rectangle(
    10,
    20,
    45,
)
```
<!-- .element: data-id="code" -->

Thus, by enforcing that a parameter like rotation can only be passed in as a positional argument, this refactoring would no longer be a breaking change,

------
<!-- .element: data-auto-animate -->
```python [9-13]
def rectangle(
    width,
    height,
    rotation_in_degrees=0,
    /,
):
    ...

rectangle(
    10,
    20,
    45,
)
```
<!-- .element: data-id="code" -->

With the trade off being that our functions couldn't use keyword arguments.

------
<!-- .element: data-auto-animate -->
```python []
def rectangle(
    width,
    height,
    rotation=0,
):
    rotation_in_degrees=rotation
    ...

rectangle(
    height=10,
    width=20,
    rotation=45,
)
```
<!-- .element: data-id="code" -->

Another case is when we want to keep the external argument name the same, and change the internal parameter name within our function.

------
<!-- .element: data-auto-animate -->
```python [4,6]
def rectangle(
    width,
    height,
    rotation=0,
):
    rotation_in_degrees=rotation
    ...

rectangle(
    height=10,
    width=20,
    rotation=45,
)
```
<!-- .element: data-id="code" -->

And we could do that by setting this parameter to another variable at the top of the function.

------
<!-- .element: data-auto-animate -->
```python [7-8]
def rectangle(
    width,
    height,
    rotation=0,
):
    rotation_in_degrees=rotation
    print(rotation_in_degrees)
    print(rotation)
    ...

rectangle(
    height=10,
    width=20,
    rotation=45,
)
```
<!-- .element: data-id="code" -->

However this can become messy, and the reference to the original parameter is still kept.

------
<!-- .slide: data-background-image="images/sad-python.png"-->

This is another case where you could argue that Python isn't perfect.

------
<!-- .slide: data-background-image="images/swift_logo.svg"-->

If we look at other languages like Swift, then this concept of naming parameters different from arguments does exist!

------
<!-- .element: data-auto-animate -->
```swift [1]
// swift
func rectangle(
    width: Int,
    height: Int,
    rotation: Int = 0
) -> Rectangle {
    let rotationInDegrees = rotation
    print(rotationInDegrees)
    print(rotation)
}

rectangle(
    width: 20,
    height: 10,
    rotation: 45
)
```
<!-- .element: data-id="code" -->

If we convert our previous python rectangle example to swift...

------
<!-- .element: data-auto-animate -->
```swift [7]
// swift
func rectangle(
    width: Int,
    height: Int,
    rotation: Int = 0
) -> Rectangle {
    let rotationInDegrees = rotation
    print(rotationInDegrees)
    print(rotation)
}

rectangle(
    width: 20,
    height: 10,
    rotation: 45
)
```
<!-- .element: data-id="code" -->

Then instead of creating a new variable to re-name the parameter

------
<!-- .element: data-auto-animate -->
```swift [5,7]
// swift
func rectangle(
    width: Int,
    height: Int,
    rotation rotationInDegrees: Int = 0
) -> Rectangle {
    print(rotationInDegrees)
}

rectangle(
    width: 20,
    height: 10,
    rotation: 45
)
```
<!-- .element: data-id="code" -->

An argument label can be used that's internal to the function

------
<!-- .element: data-auto-animate -->
```swift [13]
// swift
func rectangle(
    width: Int,
    height: Int,
    rotation rotationInDegrees: Int = 0
) -> Rectangle {
    print(rotationInDegrees)
}

rectangle(
    width: 20,
    height: 10,
    rotation: 45
)
```
<!-- .element: data-id="code" -->

Avoiding the need to change the interface,

------
<!-- .element: data-auto-animate -->
```swift [7]
// swift
func rectangle(
    width: Int,
    height: Int,
    rotation rotationInDegrees: Int = 0
) -> Rectangle {
    print(rotationInDegrees)
}

rectangle(
    width: 20,
    height: 10,
    rotation: 45
)
```
<!-- .element: data-id="code" -->

or create additional variables.

------
<!-- .element: data-auto-animate -->
```python [4]
def rectangle(
    width,
    height,
    rotation rotation_in_degrees=0,
):
    print(rotation_in_degrees)
    ...

rectangle(
    height=10,
    width=20,
    rotation=45,
)
```
<!-- .element: data-id="code" -->

Wouldn't it be awesome if we could do the same thing in Python?

------
<!-- .slide: data-background-image="images/javascript-logo.png"-->

This feature also exists in Javascript

------
<!-- .element: data-auto-animate -->
```javascript [1,5]
// javascript
function rectangle({
    width,
    height,
    rotation: rotationInDegrees=0,
}) {
    console.log(rotationInDegrees)
}

rectangle({
    width: 10,
    height: 20,
    rotation: 45,
});
```
<!-- .element: data-id="code" -->

It looks like this, which is quite similar.

But for those of you unfamiliar with JavaScript, the way it works is quite different.

------
<!-- .element: data-auto-animate -->
```javascript [1,6,10,14]
// javascript
function rectangle({
    width,
    height,
    rotation: rotationInDegrees=0,
}) {
    console.log(rotationInDegrees)
}

rectangle({
    width: 10,
    height: 20,
    rotation: 45,
});
```
<!-- .element: data-id="code" -->

And the secret is in these braces.

------
<!-- .element: data-auto-animate -->
```javascript [1,10-15]
// javascript
function rectangle({
    width,
    height,
    rotation: rotationInDegrees=0,
}) {
    console.log(rotationInDegrees)
}

const obj = {
    width: 10,
    height: 20,
    rotation: 45,
};
rectangle(obj);
```
<!-- .element: data-id="code" -->

Because these braces really define an object (like a python dictionary)

------
<!-- .element: data-auto-animate -->
```javascript [1,2]
// javascript
function rectangle(parameter) {
    const {
        width,
        height,
        rotation: rotationInDegrees=0,
    } = parameter;
    console.log(rotationInDegrees)
}

const obj = {
    width: 10,
    height: 20,
    rotation: 45,
};
rectangle(obj);
```
<!-- .element: data-id="code" -->

So really, there's only ever been one argument to this function.

------
<!-- .element: data-auto-animate -->
```javascript [1,3-7]
// javascript
function rectangle(parameter) {
    const {
        width,
        height,
        rotation: rotationInDegrees=0,
    } = parameter;
    console.log(rotationInDegrees)
}

const obj = {
    width: 10,
    height: 20,
    rotation: 45,
};
rectangle(obj);
```
<!-- .element: data-id="code" -->

And what's happening here, is that the

------
<!-- .element: data-auto-animate -->
```javascript [12-14]
// javascript
function rectangle(parameter) {
    const {
        width,
        height,
        rotation: rotationInDegrees=0,
    } = parameter;
    console.log(rotationInDegrees)
}

const obj = {
    width: 10,
    height: 20,
    rotation: 45,
};
rectangle(obj);
```
<!-- .element: data-id="code" -->

values of this object being passed in,

------
<!-- .element: data-auto-animate -->
```javascript [4-5]
// javascript
function rectangle(parameter) {
    const {
        width,
        height,
        rotation: rotationInDegrees=0,
    } = parameter;
    console.log(rotationInDegrees)
}

const obj = {
    width: 10,
    height: 20,
    rotation: 45,
};
rectangle(obj);
```
<!-- .element: data-id="code" -->

are being destructed into the variables width and height,

------
<!-- .element: data-auto-animate -->
```javascript [6]
// javascript
function rectangle(parameter) {
    const {
        width,
        height,
        rotation: rotationInDegrees=0,
    } = parameter;
    console.log(rotationInDegrees)
}

const obj = {
    width: 10,
    height: 20,
    rotation: 45,
};
rectangle(obj);
```
<!-- .element: data-id="code" -->

with rotation being re-assigned to a different name

------
<!-- .element: data-auto-animate -->
```javascript [1,3-5]
// javascript
function rectangle(parameter) {
    const width = parameter.width;
    const height = parameter.height;
    const rotationInDegrees = parameter.rotation;
    console.log(rotationInDegrees)
}

const obj = {
    width: 10,
    height: 20,
    rotation: 45,
};
rectangle(obj);
```
<!-- .element: data-id="code" -->

which in effect, is like assigning the variables from an object individually.

------
```javascript []
// javascript
function rectangle({
    width,
    height,
    rotation: rotationInDegrees=0,
}) {
    console.log(rotationInDegrees)
}

rectangle({
    width: 10,
    height: 20,
    rotation: 45,
});
```
<!-- .element: data-id="code" -->

Okay so why am I explaining all this?

------
<!-- .element: data-auto-animate -->
```python [8-13]
def rectangle(
    width,
    height,
    rotation=0,
):
    ...

params = {
    "height": 10,
    "width": 20,
    "rotation": 45,
}
rectangle(**params)
```
<!-- .element: data-id="code" -->

Because Python let's you do this with dictionaries too!

------
<!-- .element: data-auto-animate -->
```python [13]
def rectangle(
    width,
    height,
    rotation=0,
):
    ...

params = {
    "height": 10,
    "width": 20,
    "rotation": 45,
}
rectangle(**params)
```
<!-- .element: data-id="code" -->

By using the `**` operator within a function call, python will unpack the keys of the dictionary as the keywords, and the values as the arguments.

------
<!-- .slide: data-background-image="images/thinking.svg"-->

This might make you wonder, what happens if extra properties are passed into these function calls?

------
<!-- .element: data-auto-animate -->
```javascript [1,3-5,12]
// javascript
function rectangle({
    width,
    height,
    rotation,
});

rectangle({
    width: 10,
    height: 20,
    rotation: 45,
    extra: "argument",
});
```
<!-- .element: data-id="code" -->

Well, I'm sorry to disappoint you, but in JavaScript, the answer is... nothing. They don't get unpacked and thus they're ignored.

------
<!-- .element: data-auto-animate -->
```javascript [6]
// javascript
function rectangle({
    width,
    height,
    rotation,
    ...rest,
});

rectangle({
    width: 10,
    height: 20,
    rotation: 45,
    extra: "argument",
});
```
<!-- .element: data-id="code" -->

But, there is a way to keep them, and that is by using the ellipses `...rest` property.

------
<!-- .element: data-auto-animate -->
```javascript [4]
// javascript
function rectangle({
    width,
    height,
    rotation,
    ...rest, // { extra: "argument" }
});

rectangle({
    width: 10,
    height: 20,
    rotation: 45,
    extra: "argument",
});
```
<!-- .element: data-id="code" -->

Allowing us to save the remaining properties for whatever they may be needed for.

------
<!-- .element: data-auto-animate -->
```python [12]
def rectangle(
    width,
    height,
    rotation=0,
):
    ...

params = {
    "height": 10,
    "width": 20,
    "rotation": 45,
    "extra": "argument",
}
rectangle(**params)
```
<!-- .element: data-id="code" -->

But if this is how JavaScript named parameters work, what happens in python, if we pass extra keyword arguments into a python function?

------
<!-- .element: data-auto-animate -->
```python [12,14]
def rectangle(
    width,
    height,
    rotation=0,
):
    ...

params = {
    "height": 10,
    "width": 20,
    "rotation": 45,
    "extra": "argument,
}
# TypeError: rectangle() got an unexpected keyword argument 'extra'
rectangle(**params)
```
<!-- .element: data-id="code" -->

Well, unlike JavaScript, we'll get an error, telling us off that we passed in an unexpected keyword argument, which you could argue is pretty good default behavior!

And I say default here because you can also specify a way to keep these leftover arguments,

------
<!-- .element: data-auto-animate -->
```python [5]
def rectangle(
    width,
    height,
    rotation=0,
    **rest,
):
    ...

params = {
    "height": 10,
    "width": 20,
    "extra": "argument",
}
rectangle(**params)
```
<!-- .element: data-id="code" -->

and that is by using our good friend `**` again, adding it to a `rest` parameter.

------
<!-- .element: data-auto-animate -->
```python [5]
def rectangle(
    width,
    height,
    rotation=0,
    **rest, # { "extra": "argument" }
):
    ...

params = {
    "height": 10,
    "width": 20,
    "extra": "argument",
}
rectangle(**params)
```
<!-- .element: data-id="code" -->

which captures any extra keyword arguments into a dictionary

As a side note, similar to javascript, this parameter doesn't have to be called `rest` either.

------
<!-- .element: data-auto-animate -->
```python [5]
def rectangle(
    width,
    height,
    rotation=0,
    **kwargs, # { "extra": "argument" }
):
    ...

params = {
    "height": 10,
    "width": 20,
    "extra": "argument",
}
rectangle(**params)
```
<!-- .element: data-id="code" -->

The general convention in Python is `kwargs` for keyword args.

------
<!-- .element: data-auto-animate -->
```python [2]
def rectangle(
    { width, height }, # SyntaxError: invalid syntax
    height,
    rotation=0,
    **kwargs,
):
    ...

params = {
    "height": 10,
    "width": 20,
    "extra": "argument",
}
rectangle(**params)
```
<!-- .element: data-id="code" -->

And unlike JavaScript, Python doesn't currently have a way to unpack parameters within function definitions.

------
<!-- .slide: data-background-image="images/good-old-days.png"-->

But fun fact, it did used to in python 2! https://peps.python.org/pep-3113/

------
<!-- .element: data-auto-animate -->
```python []
def rectangle(
    (width, height),
):
    print "width:", width, "height:", height

rectangle((10, 20)) # width: 10 height: 20
```
<!-- .element: data-id="code" -->

Well... it was only for tuples

But who knows, maybe it'll come back to Python 3 after a PEP?

Anyways where were we...

------
<!-- .element: data-auto-animate -->
```python [14]
def rectangle(
    width,
    height,
    rotation=0,
    **kwargs, # { "extra": "argument" }
):
    ...

params = {
    "height": 10,
    "width": 20,
    "extra": "argument",
}
rectangle(**params)
```
<!-- .element: data-id="code" -->

A question you may have about `**` is,

------
<!-- .element: data-auto-animate -->
```python [15-17]
def rectangle(
    width,
    height,
    rotation=0,
    **kwargs,
):
    ...

params = {
    "height": 10,
    "width": 20,
    "extra": "argument",
}
rectangle(
    height=30,
    width=40,
    **params
)
```
<!-- .element: data-id="code" -->

what happens if arguments are provided in the function and with the double star?

------
<!-- .element: data-auto-animate -->
```python [14]
def rectangle(
    width,
    height,
    rotation=0,
    **kwargs,
):
    ...

params = {
    "width": 10,
    "height": 20,
    "extra": "argument",
}
# TypeError: rectangle() got multiple values for keyword argument 'width'
rectangle(
    width=30,
    height=40,
    **params
)
```
<!-- .element: data-id="code" -->

Well, Python will nicely tell us that we've made a mistake.

------
<!-- .element: data-auto-animate -->
```python [14,16-17]
def rectangle(
    width,
    height,
    rotation=0,
    **kwargs,
):
    ...

params = {
    "width": 10,
    "height": 20,
    "extra": "argument",
}
# TypeError: rectangle() got multiple values for keyword argument 'width'
rectangle(
    30,
    40,
    **params
)
```
<!-- .element: data-id="code" -->

And we'll get the same error if they're passed in as positionals instead.

------
<!-- .element: data-auto-animate -->
```python [9-18]
def rectangle(
    width,
    height,
    rotation=0,
    **kwargs,
):
    ...

params = {
    "width": 10,
    "height": 20,
    "extra": "argument",
}
rectangle(
    30,
    40,
    **params
)
```
<!-- .element: data-id="code" -->

If you did want to make it such that this was okay, there is one thing you can do.

------
<!-- .element: data-auto-animate -->
```python [4]
def rectangle(
    width,
    height,
    /,
    rotation=0,
    **kwargs,
):
    ...

params = {
    "width": 10,
    "height": 20,
    "extra": "argument",
}
rectangle(
    30,
    40,
    **params
)
```
<!-- .element: data-id="code" -->

And this is the last of three cases I mentioned earlier, as another use of slash to enforce positional arguments.

------
<!-- .element: data-auto-animate -->
```python [2-3,6]
def rectangle(
    width, # 30
    height, # 40
    /,
    rotation=0,
    **kwargs, # {"width": 10, "height": 20", "extra": "argument"}
):
    ...

params = {
    "width": 10,
    "height": 20,
    "extra": "argument",
}
rectangle(
    30,
    40,
    **params
)
```
<!-- .element: data-id="code" -->

Making it such that those extra keyword arguments are forced into kwargs.

------
<!-- .element: data-auto-animate -->
```python [4,9-13]
def rectangle(
    width,
    height,
    **kwargs,
):
    ...

rectangle(
    width=10,
    height=20,
    rotation=45,
    color="green",
    line_width=10,
)
```
<!-- .element: data-id="code" -->

Now you might have noticed that **kwargs is pretty cool, since it lets us pass in an arbitrary number of arguments.

------
<!-- .element: data-auto-animate -->
```python []
sum(
    10,
    20,
    30,
    40,
)
```
<!-- .element: data-id="code" -->

But there are also cases where we can't define a keyword for every argument.

Say for example, when we want to sum a list of numbers.

------
<!-- .element: data-auto-animate -->
```python [4]
def rectangle(
    width,
    height,
    *args,
):
    ...
```
<!-- .element: data-id="code" -->

This is where `*args` comes in, which is like `**kwargs` but for positional arguments.

------
<!-- .element: data-auto-animate -->
```python [4, 11-12]
def rectangle(
    width,
    height,
    *args, # ("round", 40)
):
    ...

rectangle(
    10,
    20,
    "round", # args[0]
    40,      # args[1]
)
```
<!-- .element: data-id="code" -->

`args` then appears as a variable that holds a tuple of all the extra arguments that were passed in.

It's worth noting that by nature of `*args` capturing all additional positional arguments, any further parameters must be keyword only.

------
<!-- .element: data-auto-animate -->
```python [5]
def rectangle(
    width,
    height,
    *args, # ("round", 40)
    rotation,
):
    ...

rectangle(
    10,
    20,
    "round",
    40,
)
```
<!-- .element: data-id="code" -->

So if a new parameter is added after it...

------
<!-- .element: data-auto-animate -->
```python [9-14]
def rectangle(
    width,
    height,
    *args, # ("round", 40)
    rotation,
):
    ...

rectangle(
    10,
    20,
    "round",
    40,
)
```
<!-- .element: data-id="code" -->

and the function is run as before...

------
<!-- .element: data-auto-animate -->
```python [9]
def rectangle(
    width,
    height,
    *args,
    rotation,
):
    ...

# TypeError: rectangle() missing 1 required keyword-only argument: 'rotation'
rectangle(
    10,
    20,
    "round",
    40,
)
```
<!-- .element: data-id="code" -->

We'll get a missing keyword argument error.

------
<!-- .element: data-auto-animate -->
```python [13]
def rectangle(
    width,
    height,
    *args,
    rotation,
):
    ...

rectangle(
    10,
    20,
    "round",
    rotation=40,
)
```
<!-- .element: data-id="code" -->

Unless that argument is passed in with a keyword.

------
<!-- .element: data-auto-animate -->
```python [14]
def rectangle(
    width,
    height,
    *args,
    rotation,
):
    ...

rectangle(
    10,
    20,
    "round",
    rotation=40,
    color="green",
)
```
<!-- .element: data-id="code" -->

And if an extra keyword argument is passed in...

------
<!-- .element: data-auto-animate -->
```python [9]
def rectangle(
    width,
    height,
    *args,
    rotation,
):
    ...

# TypeError: rectangle() got an unexpected keyword argument 'color'
rectangle(
    10,
    20,
    "round",
    rotation=40,
    color="green",
)
```
<!-- .element: data-id="code" -->

We'll get an error for an unexpected keyword argument.

------
<!-- .element: data-auto-animate -->
```python [9-15]
def rectangle(
    width,
    height,
    *args,
    rotation,
):
    ...

rectangle(
    10,
    20,
    "round",
    rotation=40,
    color="green",
)
```
<!-- .element: data-id="code" -->

What if we wanted to be sure that we could always pass in all arguments?

------
<!-- .element: data-auto-animate -->
```python [6]
def rectangle(
    width,
    height,
    *args,
    rotation,
    **kwargs,
):
    ...

rectangle(
    10,
    20,
    "round",
    40,
    color="green",
)
```
<!-- .element: data-id="code" -->

Then we could end the definition with **kwargs so that our function captures both!

------
<!-- .element: data-auto-animate -->
```python [8-14]
def rectangle(
    width,
    height,
    *args,
    rotation,
    **kwargs,
):
    return shape(
        width,
        height,
        rotation,
        args,
        kwargs,
    )
```
<!-- .element: data-id="code" -->

This would let us pass in all extra arguments down to other functions.

------
<!-- .element: data-auto-animate -->
```python [13]
def rectangle(
    width,
    height,
    *args,
    rotation,
    **kwargs,
):
    return shape(
        width,
        height,
        rotation,
        args,
        **kwargs,
    )
```
<!-- .element: data-id="code" -->

And similar to `**` that allows for unpacking within a function call,

------
<!-- .element: data-auto-animate -->
```python [11]
def rectangle(
    width,
    height,
    *args,
    rotation,
    **kwargs,
):
    return shape(
        width,
        height,
        rotation,
        *args,
        **kwargs,
    )
```
<!-- .element: data-id="code" -->

We can also do the same thing with `*` to unpack into functions with variable arguments, to respect shape's function definition.

------
<!-- .slide: data-background-image="images/thinking.svg"-->

But are arbitrary keyword or positional arguments a good idea?

------
<!-- .slide: data-background-image="images/rust_logo.svg"-->

For that, we could look at the design of newer, safer, languages like rust.

------
<!-- .element: data-auto-animate -->
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
<!-- .element: data-id="code" -->


While I'm not an expert in Rust, to my understanding, Rust doesn't support variable function arguments.
Not only is it hard for the type checker, but also hard for the reader.
So if you do want this complexity, you can use lists, which don't cause variable type signatures, or macros, which pass the complexity onto the writer.

TODO: Update rust statement and emphasize point about complexity that Python allows

------
<!-- .element: data-auto-animate -->
```python [4-5,10-11]
def rectangle(
    width,
    height,
    *args,
    **kwargs,
):
    return shape(
        width,
        height,
        *args,
        **kwargs
    )
```
<!-- .element: data-id="code" -->

And this complexity is seen in Python, since they can make functions difficult to understand how they should be used, given there's no need for types.

For example what can really be passed into rectangle?

------
<!-- .element: data-auto-animate -->
```python [4-5]
def rectangle(
    width: int,
    height: int,
    *args: str,
    **kwargs: int,
):
    ...
```
<!-- .element: data-id="code" -->

Even if they are typed in their most simple form, it requires the values to be of the same type.

Which you could say for the case of args is fine, because if they needed to be typed differently

------
<!-- .element: data-auto-animate -->
```python [4-6]
def rectangle(
    width: int,
    height: int,
    name: str,
    rotation: int,
    *args: str,
    **kwargs: int,
):
    ...
```
<!-- .element: data-id="code" -->

then in most cases, the definition should be updated with those param types.

> https://docs.python.org/3/library/typing.html#typing.TypeVarTuple

------
<!-- .element: data-auto-animate -->
```python []
from typing import TypedDict, Unpack

class ShapeValues(TypedDict):
    rotation: int
    name: str

def rectangle(
    width: int,
    height: int,
    *args: str,
    **kwargs: Unpack[ShapeValues],
):
    ...
```
<!-- .element: data-id="code" -->

And for typing keyword arguments, only from Python 3.11 were additions added as support, to help specify what keywords could be caught, and what their types could be.

> https://docs.python.org/3/library/typing.html#typing.Unpack
> https://typing.python.org/en/latest/spec/callables.html#unpack-kwargs
> https://chatgpt.com/share/67ea8fb7-5874-8004-a270-1fa956b296f2

> If you're new to python, I will note for you to look into the other types of unpacking uses for this `*` operator, as that's outside the scope of this talk.
> NOTE: Could cut this ** and * content. How to segue?
> NOTE: Could use sub as the example instead of rectangle to make the statement?

------
<!-- .element: data-auto-animate -->
```python [1,10]
def function(
    positional_only,
    /, # Positional only parameter indicator
    positional_or_keyword,
    positional_or_keyword_with_default="foo",
    *arbitrary_argument_tuple, # * also indicates keyword only
    keyword_only,
    keyword_with_default="bar",
    **keyword_argument_dict,
):
```
<!-- .element: data-id="code" -->

So to recap, this is python's function argument and parameter system,

------
<!-- .element: data-auto-animate -->
```python [3]
def function(
    positional_only,
    /, # Positional only parameter indicator
    positional_or_keyword,
    positional_or_keyword_with_default="foo",
    *arbitrary_argument_tuple, # * also indicates keyword only
    keyword_only,
    keyword_with_default="bar",
    **keyword_argument_dict,
):
```
<!-- .element: data-id="code" -->

The slash special parameter marks that the previous parameters

------
<!-- .element: data-auto-animate -->
```python [2]
def function(
    positional_only,
    /, # Positional only parameter indicator
    positional_or_keyword,
    positional_or_keyword_with_default="foo",
    *arbitrary_argument_tuple, # * also indicates keyword only
    keyword_only,
    keyword_with_default="bar",
    **keyword_argument_dict,
):
```
<!-- .element: data-id="code" -->

are positional only

------
<!-- .element: data-auto-animate -->
```python [4]
def function(
    positional_only,
    /, # Positional only parameter indicator
    positional_or_keyword,
    positional_or_keyword_with_default="foo",
    *arbitrary_argument_tuple, # * also indicates keyword only
    keyword_only,
    keyword_with_default="bar",
    **keyword_argument_dict,
):
```
<!-- .element: data-id="code" -->

There's the standard parameter that can be positional or keyword,

------
<!-- .element: data-auto-animate -->
```python [5]
def function(
    positional_only,
    /, # Positional only parameter indicator
    positional_or_keyword,
    positional_or_keyword_with_default="foo",
    *arbitrary_argument_tuple, # * also indicates keyword only
    keyword_only,
    keyword_with_default="bar",
    **keyword_argument_dict,
):
```
<!-- .element: data-id="code" -->

and can also be set with a default

------
<!-- .element: data-auto-animate -->
```python [3,5]
def function(
    positional_only,
    positional_only_with_default="baz",
    /, # Positional only parameter indicator
    positional_or_keyword_with_default="foo",
    *arbitrary_argument_tuple, # * also indicates keyword only
    keyword_only,
    keyword_with_default="bar",
    **keyword_argument_dict,
):
```
<!-- .element: data-id="code" -->

as can positional only if they, and all other positional arguments are also given defaults

------
<!-- .element: data-auto-animate -->
```python [6]
def function(
    positional_only,
    /, # Positional only parameter indicator
    positional_or_keyword,
    positional_or_keyword_with_default="foo",
    *arbitrary_argument_tuple, # * also indicates keyword only
    keyword_only,
    keyword_with_default="bar",
    **keyword_argument_dict,
):
```
<!-- .element: data-id="code" -->

`*` captures an arbitrary number of positional arguments,

------
<!-- .element: data-auto-animate -->
```python [7,8]
def function(
    positional_only,
    /, # Positional only parameter indicator
    positional_or_keyword,
    positional_or_keyword_with_default="foo",
    *arbitrary_argument_tuple, # * also indicates keyword only
    keyword_only,
    keyword_with_default="bar",
    **keyword_argument_dict,
):
```
<!-- .element: data-id="code" -->

and also indicates that further parameters are keyword only

------
<!-- .element: data-auto-animate -->
```python [7]
def function(
    positional_only,
    /, # Positional only parameter indicator
    positional_or_keyword,
    positional_or_keyword_with_default="foo",
    *arbitrary_argument_tuple, # * also indicates keyword only
    keyword_only,
    keyword_with_default="bar",
    **keyword_argument_dict,
):
```
<!-- .element: data-id="code" -->

such as this keyword argument,

------
<!-- .element: data-auto-animate -->
```python [8]
def function(
    positional_only,
    /, # Positional only parameter indicator
    positional_or_keyword,
    positional_or_keyword_with_default="foo",
    *arbitrary_argument_tuple, # * also indicates keyword only
    keyword_only,
    keyword_with_default="bar",
    **keyword_argument_dict,
):
```
<!-- .element: data-id="code" -->

or this one with a default.

------
<!-- .element: data-auto-animate -->
```python [6]
def function(
    positional_only,
    /, # Positional only parameter indicator
    positional_or_keyword,
    positional_or_keyword_with_default="foo",
    *, # Keyword only parameter indicator
    keyword_only,
    keyword_with_default="bar",
    **keyword_argument_dict,
):
```
<!-- .element: data-id="code" -->

And `*` can also be used alone as a special parameter to do the same.

------
<!-- .element: data-auto-animate -->
```python [9]
def function(
    positional_only,
    /, # Positional only parameter indicator
    positional_or_keyword,
    positional_or_keyword_with_default="foo",
    *arbitrary_argument_tuple, # * also indicates keyword only
    keyword_only,
    keyword_with_default="bar",
    **keyword_argument_dict,
):
```
<!-- .element: data-id="code" -->

And finally double star, to handle arbitrary keyword arguments

------
<!-- .slide: data-background-image="images/approaching_amazing_changing_0.svg"-->

So while you can argue that Python's function system

------
<!-- .slide: data-background-image="images/approaching_amazing_changing_1.svg"-->

is both approaching,

------
<!-- .slide: data-background-image="images/approaching_amazing_changing_2.svg"-->

and amazing,

------
<!-- .slide: data-background-image="images/approaching_amazing_changing_3.svg"-->

at least it's forever changing...

------

# <br>
![args-amazing-or-approaching.nohumanerrors.com](images/args-amazing-or-approaching.nohumanerrors.com_qrcode.svg)<!-- .element: style="max-height: 95%"-->
<!-- .element: class="r-stretch"-->
## `args-amazing-or-approaching.nohumanerrors.com`
# `@ekohilas`

If you're after the resources for this talk, you can find them in these links.

Or if you're after me, you can collaborate with me on nohumanerrors.com, find me online at ekohilas, or here if you have any questions or feedback!

------

# Thanks!
![args-amazing-or-approaching.nohumanerrors.com](images/args-amazing-or-approaching.nohumanerrors.com_qrcode.svg)<!-- .element: style="max-height: 95%"-->
<!-- .element: class="r-stretch"-->
## `args-amazing-or-approaching.nohumanerrors.com`
# `@ekohilas`

Thanks to my friends, family, the open source community, as well as to you for listening!

