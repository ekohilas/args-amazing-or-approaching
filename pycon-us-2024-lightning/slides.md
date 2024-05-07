
---
# Args: Amazing or Approaching? 
<!-- .element: class="r-fit-text" -->
## Lighting Edition 
### Evan Kohilas
### @ekohilas - nohumanerrors.com

------

Where we could make our code clearer and safer, using named arguments.

> {19:30 (1:30) 8}

------

<div class="r-stack">
    <img src="images/hearts.png">
    <img src="images/python.svg">
</div>

I actually have utmost adoration for python's beautiful function argument system.

So if you let me go on a tangent here, I'll explain why....

------
```java
rectangle(
    int width,
    int height,
    int rotation
);
```

Take for example, this function, that creates a rectangle.
If we're using another language, and we want to setup rotation to default to 0

------
```java
rectangle(
    int width,
    int height
) {
    rectangle(width, height, 0);
}
```

then we often need a function override

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

But since in python, we have default arguments...

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

there's no need for chained overrides, because if we don't specify a rotation, it'll default to 0 instead.

------
```java
Rectangle.builder(height, width)
    .build();
 
```
<!-- .element: data-notrim -->

Other languages fix this problem through builders, that store and create this state,

------
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

But yet another issue lies, due to the nature of the required ordered arguments.
And that is that there's no knowing whether the arguments are set correctly 

------
```java
Rectangle.builder(width, height)
    .build();
 
```

You might have not noticed, but these arguments were swapped, and should be width and height!

------
```java
Rectangle.builder(height, width)
    .build();
 
```

Not height and width.

------
```python
rectangle(
    width=width,
    height=height,
)
```

Python resolves this with named arguments (and thus also does away with builders)

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

Thus, by always using named arguments, our code is always future proofed against errors,

------
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

Where 1, 2, and 3 were previously for height, width, and rotation

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

Naming our arguments not only lets us prevent this issue.

But also reduces issues with refactoring,

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

------
```python []
for edge in self.edges(
    port=port,
    city=city,
)
```

Now you might be wondering, what about the case where the name of the variable being passed in is named the same as the argument?

Isn't that redundant and noisy?

Well maybe this is a good opportunity to rename parameters.

------
```python []
for edge in self.edges(
    from=port,
    to=city,
)
```

Perhaps it would be more descriptive to use names like from and to, making the code more natural to read.

------
```python []
def edges(from, to):
    ...
```

But then, they might not make for great variable names inside the context of the function.

Or like in this case, where from is a keyword in python.

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

If Python learned from Swift's named parameters, then we would be able to do something like this, which lets us specify both an 


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

------
```python []
for edge in self.edges(
    port=port,
    city=city,
)
```

But if we are stuck with something like our edges function that we want to clear up, our final choice is to use linters that check whether the parameter names match the variable names used in the arguments.

------
```python []
for edge in self.edges(
    port,
    city,
)
```

Allowing us to more safely go back to using positional arguments.

------
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

If you are convinced by named arguments, then there is a way to force using them,

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

But that can be cumbersome, as it can be forgotten, can make the code messy, and would also require updating all previous functions.

------
<!-- .element: data-background-image="images/fist.gif" -->

And if you think there's a better way, you'd be right!

------
![ruff logo](images/ruff.svg)

Since we can use linters to check and correct this for us!

------

<!-- .element: data-background-image="images/sprints.svg"-->

So if all of this opened your eyes, find me afterwards so we can contribute to automatically finding and applying these guardrails and enhancements!

------

![QR](images/refactoring_qr_code.svg)<br>
github.com/ekohilas/refactoring-for-fun-and-profit
<!-- .element: class="r-fit-text" -->

And if you wanted to profit yourself, I've put up some resources here that you can reference later! 

------
# Thanks! Questions?
<!-- .element: class="r-fit-text" -->
# @ekohilas

I want to say thanks to my partner and all my friends for supporting me.

And thanks to all of you for listening!

I would love to hear any feedback that you have.

And you can find me on online at @ekohilas, or on github if you wanted to take a look at the code.

However I won't claim my code is perfect, because... I think there's always a better way!

You can also find me in person, right here, as I think we still have some time for questions!

Thank you!
