<!-- intentionally blank -->

TODO: Update html for presenting

------
# Changing `re.sub` from Python 3.13?<br>😱 What have they done! 😱
<!-- .element: class="r-fit-text" -->
### Evan Kohilas
### `@ekohilas` - `nohumanerrors.com`

Hello everyone!

I'm Evan, and as someone who's super passionate about achieving nohumanerrors.com,

------
<!-- .slide: data-background-image="images/angry.svg"-->

What they've done to re.sub from Python 3.13...

------
<!-- .slide: data-background-image="images/excited.svg"-->

really exictes me!

------
<!-- .slide: data-background-image="images/question_mark.svg"-->

So what did they do? Stay to the end to find out!

> Mayve start with the problem and then
> Why? Because it fixes the error in this code.
> What's the error?, well stay tuned to find out.
> Nah I won't do that to you

------
<!-- .slide: data-background-image="images/kidding.svg"-->

Nah I wouldn't do that to you.

------
<!-- .slide: data-background-image="images/positional_deprecated.svg"-->

What they did was deprecate passing in positional arguments.

------
<!-- .slide: data-background-image="images/but_why.gif"-->

But why?

Well that's the most exciting part for me.

And if you hear me out, you too, can learn why it should excite you!

> TODO: Split slide

------

<div class="r-stack">
    <img src="images/hearts.png">
    <img src="images/python.svg">
</div>

Full disclosure, I _might_ be biased by having the utmost adoration for python's beautiful function argument system.

---
```java
Rectangle rectangle(
    int width,
    int height,
    int rotation
);
```

To show what I mean, I'll start with a function from another language, that creates a rectangle.
In this language, if we want to setup rotation to default to 0,

------
```java
Rectangle rectangle(
    int width,
    int height
) {
    rectangle(width, height, 0);
}
```

then we often need to define an overload of the function name, that calls it with our defaults.

> TODO: remove the need for overloading?

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

But in python, since we have default arguments...

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

there's no need for chained overloads, because if we don't specify a rotation, it'll default to 0 instead.

---
```java
Rectangle.builder(height, width)
    .build();
 
```
<!-- .element: data-notrim -->

Other languages fix this problem through builders, that store and create this state,

---
```java
Rectangle.builder(height, width)
    .withRotation(rotation)
    .build();
```

resolving this issue by allowing for optionally added data.

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

(3s pause)

And that's not your fault, because for one, this is a lightning talk, and two, there's no knowing whether the arguments are set correctly, without having to reference the signature of the functions.

---
```python
rectangle(
    width=width,
    height=height,
)
```

Python is beautiful, in that it solves this with keyword arguments (and thus also does away with builders)

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

And this takes us back to `re.sub`

Can I get a show of hands if you can spot the error in this example, and didn't know before this talk?  

> TODO: Surpise code review! can you spot the error?

[That's about X of you!]

------
```python[5]
re.sub(
    r"(\w+)(\[.*?\])\s*\n(.*?)",
    replacement_function,
    content,
    re.IGNORECASE,
)
```

The error is here, with how the `re.IGNORECASE` flag is being passed in.

And if you didn't spot it, I don't blame you.

How can anyone be expected to quickly spot this error amongst so much complexity?

>  https://github.com/python/cpython/issues/56166

------
```python[8-14]
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

If we bring up the definition of re.sub,

------
```python[5,12]
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

and we look at the parameter that the flag is passed in as, you'll see it's count, not flags.

------
```python[5]
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

and then the flag is read as an int, setting the maximum number of subtitutions to 2.

------
<!-- .slide: data-background-image="images/frustrated.svg"-->

That would explain why I spent hours trying to figure out why my expected thousands of substitutions weren't working, and was instead second guessing my replacement function.

------
<!-- .slide: data-background-image="images/positional_deprecated.svg"-->

In fact, so many people have had this issue, that Python has fixed it by introducing a deprecation warning from 3.13, noting that the use of count and flags as a positional arguments will be removed and will now need to be a keyword arguments instead.

------
```python[5]
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
    count=0,
    flags=0,
)
```

So what Python is now suggesting we do, is to pass in `flags` using the keyword argument.

------
```python [12]
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

And in future, they'll likely change flags and count to be required, by adding a * in the function signature

------
```python [5,8-10]
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

What this will do, is throw us an error when we try to call the function without naming those arguments following the `*`

> TODO:
> This is only one of the few reasons why I love keyword arguments and python's beautiful function argument system
> If this alone doesn't convince you of keyword arguments, consider the case where content and pattern are swapped (for ordering) 
> Keyword arguments don't only solve problems with default positional arguments
> They also solve misordering of positional arguments
> And make fixing them easier
> And make them self documenting 

------
<!-- .slide: data-background-image="images/convinced.svg"-->

so if you've now been convinced to use keyword arguments

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

you _could_ require that in all your functions by putting `*` as the first parameter

------
<!-- .slide: data-background-image="images/agonising.svg"-->

But that can be tedious, as it can be forgotten, can make the code noisy, and would also require updating **all** previously made functions.

> TODO: Update by splitting to require `*` in one part, and then mentioning the linter rule working without star in another.

------
<!-- .element: data-auto-animate -->
```python [2, 10-11]
def rectangle(
    *
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
```python
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
<!-- .element: data-id="named" -->

it can get pretty unreadable or error prone when the number of parameters and their names are much longer

------
<!-- .element: data-auto-animate -->
```python [2]
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
<!-- .element: data-id="named" -->

Did anyone notice the typo on this line?, where the parameter and argument should both be `y`

------
<!-- .slide: data-background-image="images/ruff.svg"-->

This is where linters come in!

I **love** linters, as they're a cleaner, more pragmatic way to not only check, but also correct this for us!

------
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

For example, a rule that auto fixes all our function calls to use keyword arguments wherever possible

------
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

------
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

------
```python[3,9]
def rectangle(
    width,
    height,
):
    ...
    
rectangle(
    width,
    width, # WARN: `width` passed into parameter named `height`
)
```

and in this case, give a warning,

------
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

------
<!-- .slide: data-background-image="images/sprints.svg"-->

So if mitigating human errors excites you, I'd love to work with you in make these kinds of tools a reality!

------
<!-- .slide: data-background-image="images/inspired.svg"-->

Or, if at the least I've inspired you enough to use this paradigm in your code day to day, there's one thing worth noting. 

> TODO: Cut out?

------
```python
range(
    start=0,
    stop=10, 
    skip=2,
)   
```

You may notice in your excitement to use keyword arguments for all your function calls...

------
```python
range(
    start=0,
    stop=10, 
    skip=2,
)   

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: range() takes no keyword arguments
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

And maybe this is a call to action for removing the offending `/` special parameter,

------
```python
def range(
    start,
    stop,
    skip=1,
)
```

allowing for consistency (granted that maybe this isn't the best example)

------

# `@ekohilas`
## `args-amazing-or-approaching.nohumanerrors.com`
![args-amazing-or-approaching.nohumanerrors.com](images/args-amazing-or-approaching.nohumanerrors.com_qrcode.svg)<!-- .element: style="max-height: 95%"-->
<!-- .element: class="r-stretch"-->
# <br> 

If you can't make it to the sprints, If you're after the resources for this talk, you can find them in the links above.

Or if you're after me, you can collaborate with me on nohumanerrors.com, find me online at ekohilas, or here if you have any questions or feedback!

Or if you can't make it, you can find me online at @ekohilas, or collaborate with me on nohumanerrors.com.

------

# `@ekohilas`
## `args-amazing-or-approaching.nohumanerrors.com`
![args-amazing-or-approaching.nohumanerrors.com](images/args-amazing-or-approaching.nohumanerrors.com_qrcode.svg)<!-- .element: style="max-height: 95%"-->
<!-- .element: class="r-stretch"-->
# Thanks! 

Thanks!
