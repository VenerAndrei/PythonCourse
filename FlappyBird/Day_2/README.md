# Day two of Flappy Dot!
We tried to make the pipes but an **error**  was ocurring at drawing the rects.
[Before](/imaes/problem.png)

<hr>

# What was the problem?

We used the *pygame.draw.rect()* __WRONG__.As positions to draw the rect it required **(point_x,point_y,width,heiht)**
* **pygame.draw.rect(screen, color, (x,y,width,height), thickness)**
  * draws a rectangle
  * (x,y,width,height) is a Python tuple
  * x,y are the coordinates of the upper left hand corner
  * width, height are the width and height of the rectangle
  * thickness is the thickness of the line. If it is zero, the rectangle is filled
[After](https://i.imgur.com/bqtvRKQ.png)
