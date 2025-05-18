<!-- intentionally blank -->

> TODO: Update repo and folder name 
> TODO: Sprint submission?
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

So what did they do? I won't keep you on the hook... 

------
<!-- .slide: data-background-image="images/positional_deprecated.svg"-->

They deprecated passing in the optional arguments as positional arguments.

Can you beleive it? I can!

------
<!-- .slide: data-background-image="images/but_why.gif"-->

But why?

Well that's the most exciting part for me!

------
<!-- .slide: data-background-image="images/double_excited.svg"-->

And because I want you to be excited too,

let me give you, a...

------
<!-- .slide: data-background-image="images/code_review.svg"-->

suprise code review under pressure!

------
```python
re.sub(
    r"(\w+)(\[.*?\])\s*\n(.*?)",
    replacement_function,
    content,
    re.IGNORECASE,
)
```

Can I get a show of hands if you can spot the error in this example, **and** didn't know before this talk?  

Okay I don't have much time so...

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
<!-- .element: data-id="re" -->

The error is here, with how the `re.IGNORECASE` flag is being passed in.

And if you didn't spot it, I don't blame you.

How can anyone be expected to quickly spot this error under pressure and amongst so much complexity?

>  https://github.com/python/cpython/issues/56166

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
):
    ...
```
<!-- .element: data-id="re" -->

If we bring up the definition of re.sub,

------
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
):
    ...
```
<!-- .element: data-id="re" -->

and we look at the parameter that the flag is passed in as, you'll see it's count, not flags.

------
```python [5,12]
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
):
    ...
```
<!-- .element: data-id="re" -->

and then the flag is read as an int, setting the maximum number of subtitutions to 2.

------
<!-- .slide: data-background-image="images/frustrated.svg"-->

That would explain why I spent hours trying to figure out why my expected thousands of substitutions weren't working, and was instead second guessing my replacement function.

------
<!-- .slide: data-background-image="images/positional_deprecated.svg"-->

This is why Python introduced the deprecation warning, because it wasn't just me who experienced this problem.

> TODO: Add screenshot of github issue

------
<!-- .element: data-auto-animate -->
```python [5, 12]
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
):
    ...
```
<!-- .element: data-id="re" -->

So what Python is now suggesting we do, is to pass in `flags` using the keyword argument.

------
<!-- .element: data-auto-animate -->
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
):
    ...
```
<!-- .element: data-id="re" -->

And in future, they'll change flags and count to be required, by adding a * in the function definition 

------
<!-- .element: data-auto-animate -->
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
<!-- .element: data-id="re" -->

What this will do, is throw us an error when we try to call the function without naming those arguments following the `*`

------
<!-- .slide: data-background-image="images/love.svg"-->

This is actually one of the many reasons why I love keyword arguments, which is what the talk is **actually** about.

------
<!-- .slide: data-background-image="images/thinking.svg"-->

So if that didn't convince you, let me tell you more!

------
<!-- .element: data-auto-animate -->
```python [3-4]
re.sub(
    r"(\w+)(\[.*?\])\s*\n(.*?)",
    replacement_function,
    content,
    re.IGNORECASE,
)
```
<!-- .element: data-id="re" -->

What if for some arguments, such as `repl` and `string`

------
<!-- .element: data-auto-animate -->
```python [3-4]
re.sub(
    r"(\w+)(\[.*?\])\s*\n(.*?)",
    content,
    replacement_function,
    re.IGNORECASE,
)
```
<!-- .element: data-id="re" -->

Their ordering was accidentally swapped?

------
<!-- .element: data-auto-animate -->
```python [8-12]
re.sub(
    r"(\w+)(\[.*?\])\s*\n(.*?)",
    content,
    replacement_function,
    re.IGNORECASE,
)

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#    return _compile(pattern, flags).sub(repl, string, count)
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: expected string or bytes-like object, got 'function'
```
<!-- .element: data-id="re" -->

Well in this case the function would fail to run, because `re.sub` will fail to handle the string to search through being a function.

------
<!-- .element: data-auto-animate -->
```python [4]
re.sub(
    r"(\w+)(\[.*?\])\s*\n(.*?)",
    content,
    "", 
    re.IGNORECASE,
)
```
<!-- .element: data-id="re" -->

But what if it was a string?

------
<!-- .element: data-auto-animate -->
```python [2,4]
re.sub(
    r"(\w+)(\[.*?\])\s*\n(.*?)",
    replacement_function,
    content,
    re.IGNORECASE,
)
```
<!-- .element: data-id="re" -->

Or, if for the other string arguments, `pattern` and `string`

------
<!-- .element: data-auto-animate -->
```python [2,4]
re.sub(
    content,
    replacement_function,
    r"(\w+)(\[.*?\])\s*\n(.*?)",
    re.IGNORECASE,
)
```
<!-- .element: data-id="re" -->

they were swapped?

We'd never know there's a problem unless we knew the function definition!

------
```python [2-5]
re.sub(
    string=content,
    repl=replacement_function,
    pattern=r"(\w+)(\[.*?\])\s*\n(.*?)",
    flags=re.IGNORECASE,
)
```
<!-- .element: data-id="re" -->

So by always using keyword arguments,

------
<!-- .element: data-auto-animate -->
```python [2-5]
re.sub(
    string=content,
    repl=replacement_function,
    pattern=r"(\w+)(\[.*?\])\s*\n(.*?)",
    flags=re.IGNORECASE,
)
```
<!-- .element: data-id="re" -->

not only does the ordering now become redundant!

------
<!-- .element: data-auto-animate -->
```python [2-5]
re.sub(
    flags=re.IGNORECASE,
    pattern=r"(\w+)(\[.*?\])\s*\n(.*?)",
    repl=replacement_function,
    string=content,
)
```
<!-- .element: data-id="re" -->

Allowing us to order them however we want,

------
<!-- .element: data-auto-animate -->
```python 
re.sub(
    string=content,
    repl=replacement_function,
    pattern=r"(\w+)(\[.*?\])\s*\n(.*?)",
    flags=re.IGNORECASE,
)
```
<!-- .element: data-id="re" -->

But our usage is now self documenting,

------
<!-- .element: data-auto-animate -->
```python [4]
re.sub(
    string=content,
    repl=replacement_function,
    pattern=r"(\w+)(\[.*?\])\s*\n(.*?)",
    flags=re.IGNORECASE,
)
```
<!-- .element: data-id="re" -->

labels constant arguments,

------
<!-- .element: data-auto-animate -->
```python
re.sub(
    string=content,
    repl=replacement_function,
    pattern=r"(\w+)(\[.*?\])\s*\n(.*?)",
    flags=re.IGNORECASE,
)
```
<!-- .element: data-id="re" -->

**and**,

------
<!-- .element: data-auto-animate -->
```python
rectangle(
    height=10,
    width=20,
    opacity=1,
    color="green",
)
```
<!-- .element: data-id="re" -->

if this was a function we defined ourselves,

------
<!-- .element: data-auto-animate -->
```python []
rectangle(
    height=10,
    width=20,
    opacity=1,
    color="green",
)

def rectangle(
    height,
    width,
    opacity,
    color,
):
    ...
```
<!-- .element: data-id="re" -->

and the parameter ordering was important,

------
<!-- .element: data-auto-animate -->
```python [2-3,9-10]
rectangle(
    height=10,
    width=20,
    opacity=1,
    color="green",
)

def rectangle(
    width,
    height,
    opacity,
    color,
):
    ...
```
<!-- .element: data-id="re" -->

then when refactoring, we only have to make the changes to the definition, and not all the calls across a codebase. 

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
    width=1,
    height=2,
)
```
<!-- .element: data-id="named" -->

you _could_ require that in all your functions by putting `*` as the first parameter

------
<!-- .slide: data-background-image="images/agonising.svg"-->

But that can be tedious, as it can be forgotten, can make the code noisy, and would also require updating **all** previously made functions.

> TODO: Update by splitting to require `*` in one part, and then mentioning the linter rule working without star in another.

------
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
<!-- .element: data-id="typo" -->

it can get pretty unreadable or error prone when the number of parameters and their names are much longer

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
<!-- .element: data-id="typo" -->

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

or bring clarity by autofixing with a keyword argument.

------
<!-- .slide: data-background-image="images/sprints.svg"-->

So if mitigating human errors excites you, I'd love to collaborate with you, such as at the sprints, in working on these kinds of tools!

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

If you're after the resources for this talk, want to watch it's longer form, or you want to get in touch with either questions, feedback, or to collaborate, find me at @ekohilas or go to nohumanerrors.com!

------

# `@ekohilas`
## `args-amazing-or-approaching.nohumanerrors.com`
![args-amazing-or-approaching.nohumanerrors.com](images/args-amazing-or-approaching.nohumanerrors.com_qrcode.svg)<!-- .element: style="max-height: 95%"-->
<!-- .element: class="r-stretch"-->
# Thanks! 

Thanks!
