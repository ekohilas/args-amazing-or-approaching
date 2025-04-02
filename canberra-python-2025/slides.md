<!-- intentionally blank -->

> TODO: Update html for presenting
> TODO: Spellcheck
> TODO: Fix sectioning
> TODO: Ensure height and width are ordered where they're meant to be

------

# Args: Amazing or Approaching? 
<!-- .element: class="r-fit-text" -->
### Evan Kohilas
### `@ekohilas` - `nohumanerrors.com`

Hello everyone!

As someone who's passionate about working towards nohumanerrors.com,

> TODO: Change intro
> TODO: Newline title

------

<div class="r-stack">
    <img src="images/hearts.png">
    <img src="images/python.svg">
</div>

I have utmost adoration for python's beautiful function argument system.

---
```python
def function(
    a,
    b,
):
    ...
```

Just look at it, isn't it great? Okay I'm not that crazy, ... at least I think.
Anyways, let's get some formalities out of the way. 

------
```python [2-3]
def function(
    a,
    b,
):
    ...
```

Anyone know what the name of these are called?

Anyone else thought they were called arguments?

Yeah it still gets me, so don't fault me if I get confused!

---
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

Okay so, anyone want to take a guess at what these are called?

Yeah these are arguments!

---
```python
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

Okay now that that's out of the way let's go back to python's beautiful function argument system, that maybe I am crazy for...

---
```java
void function(
    int a,
    int b,
) {
    // function code
}
```

To show what I mean, I'll start by using a function from another language.

---
```java
void rectangle(
    int width,
    int height,
) {
    // function code
}
```

And I'll change it up to a more concrete, relatable example, making rectangles!

---
```java
void rectangle(
    int width,
    int height,
);
```

I'll also simplify it down to just the signature.

---
```java [6]
void rectangle(
    int width,
    int height,
);

basic_rectangle = rectangle(10, 20);
```

And now, this function can be called to create a basic rectangle of a particular width and height.

---
```java
void rectangle(
    int width,
    int height,
);

basic_rectangle = rectangle(10, 20);
```

But let's say that a basic rectangle isn't good enough. And we've been asked to create a rotated one instead.

> TODO: Change return type signature of rectangle
> TODO: Update variable name

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
```java [8]
void rectangle(
    int width,
    int height,
    int rotation
);

basic_rectangle = rectangle(10, 20);
rotated = rectangle(10, 20, 45);
```

Now we can make a rotated rectangle!

---
```java [7]
void rectangle(
    int width,
    int height,
    int rotation
);

basic_rectangle = rectangle(10, 20);
rotated = rectangle(10, 20, 45);
```

But now our previous function call needs to be updated.

---
```java [7]
void rectangle(
    int width,
    int height,
    int rotation
);

basic_rectangle = rectangle(10, 20, 0);
rotated = rectangle(10, 20, 45);
```

And this creates a problem, because we now need to go through and update all existing function calls for any unrotated rectangles, and add an additional argument for a default rotation of 0

---
```java
void rectangle(
    int width,
    int height,
    int rotation
);

basic_rectangle = rectangle(10, 20, 0);
rotated = rectangle(10, 20, 45);
```

Because this is tedious work that we want to avoid, in most of these languages, there are other ways that a default rotation can be setup.

------
```java[1-5]
void rotated_rectangle(
    int width,
    int height,
    int rotation
);

void rectangle(
    int width,
    int height,
);

basic_rectangle = rectangle(10, 20);
rotated = rotated_rectangle(10, 20, 45);
```

The most basic way, is by creating a new function with this rotation parameter.

Of course, we don't want to duplicate the code that makes these rectangles.

------
```java[10-12]
void rotated_rectangle(
    int width,
    int height,
    int rotation
);

void rectangle(
    int width,
    int height
) {
    return rotated_rectangle(width, height);
}

basic_rectangle = rectangle(10, 20);
rotated = rotated_rectangle(10, 20, 45);
```

So we update the old function, such that it calls the new function

------
```java[10-12]
void rotated_rectangle(
    int width,
    int height,
    int rotation
);

void rectangle(
    int width,
    int height
) {
    return rotated_rectangle(width, height, 0);
}

basic_rectangle = rectangle(10, 20);
rotated = rotated_rectangle(10, 20, 45);
```

And sets the new parameter with a default argument, which in our case will be 0.

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
    return rotated_rectangle(width, height, 0);
}

basic_rectangle = rectangle(10, 20);
rotated = rotated_rectangle(10, 20, 45);
```

Now if we take a step back, we might start to see how this might get a bit messy. The good news is, in some languages, we can do a bit of clean up through the use of function overloading.

------
```java[1-4,7-9]
void rectangle(
    int width,
    int height,
    int rotation
);

void rectangle(
    int width,
    int height
) {
    return rectangle(width, height, 0);
}

basic_rectangle = rectangle(10, 20);
rotated = rectangle(10, 20, 45);
```

With function overloading, we can define multiple functions with the same name, but different type signatures.

------
```java[11,14,15]
void rectangle(
    int width,
    int height,
    int rotation,
);

void rectangle(
    int width,
    int height,
) {
    return rectangle(width, height, 0);
}

basic_rectangle = rectangle(10, 20);
rotated = rectangle(10, 20, 45);
```

This removes the need for us to rename any functions, as these programming languages will determine which functions to call using the parameter types instead.

> TODO: Check code syntax, e.g. trailing commas

------
```python
def rectangle(
    width: int,
    height: int,
    rotation int,
): ...

def rectangle(
    width: int,
    height: int,
):
    return rectangle(width, height, 0)

basic = rectangle(10, 20) 
rotated = rectangle(10, 20, 45)
```

If we looked at the same code in python

------
```python[14-17]
def rectangle(
    width: int,
    height: int,
    rotation int,
): ...

def rectangle(
    width: int,
    height: int,
):
    return rectangle(width, height, 0)

basic = rectangle(10, 20) 
rotated = rectangle(10, 20, 45)

# TypeError:
#  rectangle() takes 2 positional arguments but 3 were given
```

It would fail!

------
```python[1-10]
def rectangle(
    width: int,
    height: int,
    rotation int,
): ...

def rectangle(
    width: int,
    height: int,
):
    return rectangle(width, height, 0)

basic = rectangle(10, 20) 
rotated = rectangle(10, 20, 45)
```

And this is because in Python, defining a function with the same name overwrites the previous definiton.

------
> TODO: Screenshot https://pypi.org/project/multipledispatch/

While there are packages like multipledispatch that you can use to replicate function overloading

------
> TODO: Screenshot with problem face https://pypi.org/project/multipledispatch/

function overloading in general can also become problematic, for reasons that will become more apparrant later.

> TODO: fix rotation int to rotation: int

------
```python
def rotated_rectangle(
    width: int,
    height: int,
    rotation int,
): ...

def rectangle(
    width: int,
    height: int,
):
    return rotated_rectangle(width, height, 0)

basic = rectangle(10, 20) 
rotated = rotated_rectangle(10, 20, 45)
```

So without function overloading, how does Python let us simplify this?

------
```python[4]
def rotated_rectangle(
    width: int,
    height: int,
    rotation: int = 0,
): ...

def rectangle(
    width: int,
    height: int,
):
    return rotated_rectangle(width, height, 0)

basic = rectangle(10, 20) 
rotated = rotated_rectangle(10, 20, 45)
```

Well in python, the concept of default arguments is built into the lanaguage (using the equals sign in the parameter definition)

------
```python[7]
def rotated_rectangle(
    width: int,
    height: int,
    rotation: int = 0,
): ...

basic = rotated_rectangle(10, 20, 0) 
rotated = rotated_rectangle(10, 20, 45)
```

So now, if we only keep a single definition, we can remove the need for function chaining

------
```python[7]
def rotated_rectangle(
    width: int,
    height: int,
    rotation: int = 0,
): ...

basic = rotated_rectangle(10, 20) 
rotated = rotated_rectangle(10, 20, 45)
```

And then, remove the need to pass in 0, since it'll use the default instead.

------
```python[1,7,8]
def rectangle(
    width: int,
    height: int,
    rotation: int = 0,
): ...

basic = rectangle(10, 20) 
rotated = rectangle(10, 20, 45)
```

Then we can rename our function back to rectangle, to get our beautiful definition.

------
```python
def rectangle(
    width: int,
    height: int,
    rotation: int = 0,
): ...

basic = rectangle(10, 20) 
rotated = rectangle(10, 20, 45)
```

As a side note, Python is not all sunshine and rainbows either (I don't think any language is!)

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

> TODO: Update types to be similar to other code
> TODO: Update to highlight metadata

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
```python [12-13]
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

Instead, their metadata ends up being the same.

That's because these default parameters are instantiated at the time the function is defined, instead of when the function is called.

Giving this strange outcome, where all functions are sharing the same state.

------
```python[4]
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

This is because in Python, the values for these default paramters are created when the function is defined, **not** when it's called.

------
```python[4,6-7]
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
big = rectangle(200, 100)

print(small.metadata) # {"width": 200, "height": 100"}
print(big.metadata)   # {"width": 200, "height": 100"}
```

So if your functions need mutable defaults, the best way to do so is to default them to None, and set the mutable that you want if it hasn't been specified.

------
```java
void rectangle(
    int width,
    int height,
);

basic_rectangle = rectangle(10, 20);
```

Now if we step away from the thunderstorms and lightning (which are very very freightening), and go back to our original example, those of you that are experienced might be thinking of another way that defaults can be done. 

> TODO: Link all code
> TODO: Finalise code examples
> TODO: Add highlighting to code examples 
> TODO: add comic effect for thunderstorms

---
```java
Rectangle.builder(height, width)
    .build();
 
```
<!-- .element: data-notrim -->

And that is through a programming construct called the builder pattern.

> TODO: use var rectangle = Rectange\n.builder otherwise not clear it's not a definition.

---
```java[1]
Rectangle.builder(height, width)
    .build();
 
```
<!-- .element: data-notrim -->

On initiation, it requires and stores all nesscary data

---
```java[2]
Rectangle.builder(height, width)
    .withRotation(rotation)
    .build();
```
<!-- .element: data-notrim -->

and then allows for adding of any optional data

---
```java[3]
Rectangle.builder(height, width)
    .withRotation(rotation)
    .build();
```
<!-- .element: data-notrim -->

before building the final state.

------
```java
Rectangle.builder(height, width)
    .build();
 
```
<!-- .element: data-notrim -->

But yet another issue lies with required arguments, that even builders can't fix.

Can anyone spot the error here?

(water break)

[No one noticed, that when I defined this builder, the ordering of height and width were swapped?]

[Yes well done] It should be width and height,

------
<!-- .element: data-auto-animate -->
```java [2-3,6]
void rectangle(
    int width,
    int height
);

Rectangle.builder(height, width)
    .build();
```
<!-- .element: data-id="builder" -->

Not height and width.

(pause for effect)

---
```java
void rectangle(
    int width,
    int height,
);

void rectangle(
    int height,
    int width,
    int rotation,
);

shape_1 = rectangle(10, 20);
shape_2 = rectangle(20, 10, 45);
```
<!-- .element: data-notrim -->

Going one step further, this same issue is what can cause function overloading to be harmful.

For example, both of these are valid definitions,

---
```java [2-3,7-8]
void rectangle(
    int width,
    int height,
);

void rectangle(
    int height,
    int width,
    int rotation,
);

shape_1 = rectangle(10, 20);
shape_2 = rectangle(20, 10, 45);
```
<!-- .element: data-notrim -->

the only difference being the ordering of the paramters

---
```java[13]
void rectangle(
    int width,
    int height,
);

void rectangle(
    int height,
    int width,
    int rotation,
);

shape_1 = rectangle(10, 20);
shape_2 = rectangle(20, 10);
```
<!-- .element: data-notrim -->

But as soon as we remove the rotation of the shape, the shapes dimensions are now different.

Without having to reference the signature of the functions, there's no knowing whether the arguments are set correctly.

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

But even in the cases where you're not refactoring, not using keyword arguments has led to errors.

------
```python
re.sub(
    r"(\w+)(\[.*?\])\s*\n(.*?)",
    replacement_function,
    content,
    re.IGNORECASE,
)
```

Can anyone spot the error in this example?
(and if you already know then let others have a chance)

[Yes it's how the flag is being passed in!]

>  https://github.com/python/cpython/issues/56166

------
```python[8-14]
re.sub(
    r"(\w+)(\[.*?\])\s*\n(.*?)",
    replacement_function,
    content,
    re.IGNORECASE,
)

re.sub(
    pattern,
    repl,
    string,
    count=0,
    flags=0,
)
```

If we bring up the definition of re.sub,

------
```python[5,12]
re.sub(
    r"(\w+)(\[.*?\])\s*\n(.*?)",
    replacement_function,
    content,
    re.IGNORECASE,
)

re.sub(
    pattern,
    repl,
    string,
    count=0,
    flags=0,
)
```

and we look at the parameter that the flag is passed in as, you'll see it's count, not flags.

------
```python[5]
re.sub(
    r"(\w+)(\[.*?\])\s*\n(.*?)",
    replacement_function,
    content,
    re.IGNORECASE, # 2
)

re.sub(
    pattern,
    repl,
    string,
    count=0,
    flags=0,
)
```

and then the flag is read as an int, setting the maximum number of subtitutions to 2.

That would explain why I spent hours trying to figure out why my expected thousands of substitutions weren't working, and was instead second guessing my replacement function.

------
> TODO: Screenshot deprecation warning https://docs.python.org/3/library/re.html#re.sub

In fact, so many people have had this issue, that Python has fixed it by introducing a deprecation warning from 3.13, noting that the use of count and flags as a positional argument will be removed and needs to be a keyword instead.

------
```python[5,13]
re.sub(
    r"(\w+)(\[.*?\])\s*\n(.*?)",
    replacement_function,
    content,
    flags=re.IGNORECASE,
)

re.sub(
    pattern,
    repl,
    string,
    *,
    count=0,
    flags=0,
)
```

And the way that they will do that, is to put `*` as a parameter before count and flags.

------
```python
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

What this will do, is throw us an error when we try to call the function without naming those arguments.

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
    height=1,
    width=2,
)
```
<!-- .element: data-id="named" -->

then one way you could force that, is by putting `*` as the first parameter,

---
> TODO: anogising emoji face

But that can be cumbersome, as it can be forgotten, can make the code noisy, and would also require updating all previously made functions.

---
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

---
<!-- .element: data-auto-animate -->
```python
rectangle(
    top_left_pos_from_x_origin=top_left_pos_from_x_origin,
    top_left_pos_from_y_origin=top_left_pos_from_y_origin,
    bottom_right_pos_from_x_origin=bottom_right_pos_from_x_origin,
    bottom_right_pos_from_y_origin=bottom_right_pos_from_y_origin,
    rotation_in_radians=rotation_in_radians,
    color_in_hex=color_in_hex,
    line_thickness_in_pixels=line_thickness_in_pixels,
)
```
<!-- .element: data-id="named" -->

it can get pretty unreadable when the number of parameters and their names are much longer

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

The good news is, for when we don't have control over the interface, PEP736 is currently debating either using something like a trailing = for arguments that should take from existing variable names

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

or adding `*` as an argument, to signify that every argument afterwards should be looked up from a variable name.

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

But given the way Python has been built, it might not be currently possible, or they might just need your help to do so!

------
![ruff logo](images/ruff.svg)

So until something changes, I personally feel that linters are a cleaner, more pragmatic way to not only check, but also correct this for us!

---
```python[8-9]
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

For example, a rule that auto fixes all our function calls to use keyword arguments wherever possible

---
```python[2-3,8-9]
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

Or, if you want the safety without the redundancy, a rule that checks that for every given positional argument, it's name is the same as the corresponding parameter.

---
```python[2,8]
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

Which would pass in this case,

---
```python[3,9]
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

and in this case, give a warning,

---
```python[3,9]
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

or bring clarity with a keyword argument.

---
<!-- .element: data-background-image="images/sprints.svg"-->

So if mitigating human errors excites you, I'd love to work with you in make these kinds of tools a reality!

> TOOD: Update image to github
> TODO: Could expand? e.g. this is because these lint rules can analyse the definitions during the calls of functions


------
> TODO: Image of influence or tips

Or, if I've influenced you enough to start using this paradigm in your code day to day, here are some things that may be worth noting. 

------
```python
range(
    start=0,
    stop=10,
    skip=2,
)   
```

For one, you may notice in your excitement to use keyword arguments for all your function calls...

------
```python
>>> range(start=0, stop=10, skip=2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: range() takes no keyword arguments
```

that not _all_ functions are happy with that.

------
```python[5]
def range(
    start,
    stop,
    skip=1,
    /,
)
```

This is because of another special parameter, `/`.
Unlike `*` which makes all further parameters keyword only,
`/` prevents all previous parameters from being passed into using keyword arguments.

------
> TODO: But why gif

Given the wonders you've just seen with keyword arguments, you might be wondering, when is this helpful?

Well there's two cases that I've seen

------
```python
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

The first may be made apparant if we had to refactor our function and change the name of our paramters.

------
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

For example, we may want to change the specification, and be more specific that the rotation is in degrees, not radians.

------
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

If we updated the name of our parameter, now any calls that pass in the `rotation` argument would now fail.

------
```python [5]
def rectangle(
    width,
    height,
    rotation_in_degrees=0,
    /,
):
    ...
    
rectangle(
    height=10,
    width=20,
    rotation=45,
)
```

Thus, by enforcing that a parameter like rotation can only be passed in as a positional argument, this refactoring would no longer be a breaking change,

------
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

With the trade off being that our functions couldn't use keyword arguments.

------
```python
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

Another case may be where we want to keep the external argument name the same, and change the internal parameter name within our function.

------
```python[4,6]
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

And we could do that by setting this parameter to another variable at the top of the function.

------
```python[7-8]
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

However this can become messy, and the reference to the original paramter is still kept.

---
> TODO: Sad python

This is another case where you could argue that Python isn't perfect.

------
```swift
func map(
    iterable: [Double],
    function: (Double) -> Double
) -> [Double] {}

map(
    iterable: [-0.5, 0.5, 1.5],
    function: round
)
```

If we look at other languages like Swift, then this concept exists as argument labels and paramter names.

------
```swift[8]
func map(
    iterable: [Double],
    function: (Double) -> Double
) -> [Double] {}

map(
    iterable: [-0.5, 0.5, 1.5],
    function: round
)
```

In this case, map is called with the argument label, `function`,

------
```swift[3]
func map(
    iterable: [Double],
    function: (Double) -> Double
) -> [Double] {}

map(
    iterable: [-0.5, 0.5, 1.5],
    function: round
)
```

which is taken from the parameter name.

------
```swift[3]
func map(
    iterable: [Double],
    with function: (Double) -> Double
) -> [Double] {}

map(
    iterable: [-0.5, 0.5, 1.5],
    with: round
)
```

But in Swift, we can also specify the argument label as `with` for that paramter 

------
```swift[8]
func map(
    iterable: [Double],
    with function: (Double) -> Double
) -> [Double] {}

map(
    iterable: [-0.5, 0.5, 1.5],
    with: round
)
```

Now, when map is called, it's done so using this label

------
```swift[6-9]
func map(
    iterable: [Double],
    with function: (Double) -> Double
) -> [Double] {}

map(
    iterable: [-0.5, 0.5, 1.5],
    with: round
)
```

I think this is awesome because I find reads so nicely!

"map this iterable with the round function."

------
```python[3,8]
def map(
    iterable: list[float],
    with function: typing.Callable[float],
) -> list[float]: ...
    
map(
    iterable=[-0.5, 0.5, 1.5],
    with=round,
)
```

Imagine if Python had this functionality. Oh how much more readable python could be!

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

For those unfamiliar with javascript, there's quite a bit going on here, so let's unpack it together.

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

In fact, Python let's you do this with dictionaries too!

------

By using the `**` operator within a function call, python will unpack the keys of the dictionary as the keywords, and the values as the arguments.

------

This might make you wonder, what happens if extra properties are passed into these function calls?

Well, I'm sorry to dissapoint you, but in javascript, the answer is, nothing. They don't get unpacked and thus they're ignored.

Buut, there is a way to keep them, and that is by using the ellipses `...rest` property.

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

But who knows, maybe it'll come back to Python 3 after a PEP?

Anyways where were we...

So, by specifying `**kwargs` as the last parameter, what this does, it tell python that any additional arguments that were passed in as keywords, and not caught by previous parameters will now be caught by `kwargs`.

What do I mean by this?

Remember how I mentioned earlier that there was two cases where you might want a `/` in your parameters?

Well, the second case is where you have a definition like this, both with a normal paramter and `**kwargs`.

And when you call this function with only keyword paramters, that first argument would be captured by the first paramter.

If you instead wanted this keyword argument to be captured by **kwargs, you can use the `/` operator to specify that that parameter (and everything before the slash) is positional only.

Now you might have noticed that **kwargs is pretty cool, since it lets us pass in an arbitatry number of arguments.

But there are also cases where we can't define a keyword for every argument.

Say for example, when we want to sum a list of numbers.

This is where `*args` comes in, which is like **kwargs but for positional arguments.

`args` then appears as a variable that holds a tuple of all the extra arguments that were passed in.

And similar to `**` within a function call, `*` can be used to unpack a list into these variable arguments.

Which is nesscary since if we want to pass arguments along, we can't use named arguments like args=args, or kwargs=kwargs.

It's also worth noting that by nature of `*args` capturing all additional positional arguments, any further paramters become keyword only.

You could you say that this is because of the existance of `*` within the parameters.

Because `*` can also be used by itself, similar to `/`, if you still want to mandate that futher parameters are keyword only, but didn't want to capture additional positional arguments.

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

And this can also be evident in Python, since they can make functions difficult to understand how they should be used, given there's no need for types.

------
```python
f(*args: int, **kwargs: str):
```
Even if they are typed like this, then all the values need to be of the same type.

Which you could say for the case of args is fine, because if they needed to be typed differently

> TODO: inverse int and str

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

And for typing keyword arguments, only from Python 3.11 were additions added as support, to help specify what keywords could be caught, and what their types could be.

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
    /, # Positional only parameter seperator
    positional_or_keyword,
    *aribitrary_argument_tuple: int, # Also marks further paramaters as keyword only
    keyword_only: str,
    **keyword_argument_dict: typing.Unpack[Kw]
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

If you're after the resources for this talk, you can find them in the links above.

Or if you're after me, you can collaborate with me on nohumanerrors.com, find me online at ekohilas, or here if you have any questions or feedback!

------

# Thanks! 
![pep736.nohumanerrors.com](images/pep736.nohumanerrors.com_qrcode.svg)<!-- .element: style="max-height: 95%"-->
<!-- .element: class="r-stretch"-->
# `pep736.nohumanerrors.com`
# `@ekohilas`

Thanks to my friends, family, the open source community, as well as to you for listening!


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

