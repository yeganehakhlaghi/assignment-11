import random
import arcade


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width=16
        self.height=16
        self.color1=arcade.color.SKY_BLUE
        self.color2=arcade.color.BLUE_GREEN
        self.body=[]
        self.body_size=0
        self.center_x=SCREEN_WIDTH//2
        self.center_y=SCREEN_HEIGHT //2
        self.speed = 4
        self.change_x=0
        self.change_y=0
        self.score=0


    def eat(self):
        self.body_size +=1


    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color1)
        for i,part in enumerate(self.body):
            if i%2 == 0:
                arcade.draw_rectangle_filled(part[0],part[1],self.width,self.height,self.color1)
            else:
                arcade.draw_rectangle_filled(part[0],part[1],self.width,self.height,self.color2)
    
    def move(self):
        #اضافه کردن موقعیت قبلی سر مار به لیست بدن
        self.body.append([self.center_x,self.center_y])

        if len(self.body) > self.body_size:
            self.body.pop(0)
        if self.change_x == -1:
            self.center_x -= self.speed

        elif self.change_x == 1:
            self.center_x += self.speed
        
        if self.change_y == -1:
            self.center_y -= self.speed

        elif self.change_y == 1:
            self.center_y += self.speed

        if self.center_y < 0:
            self.center_y=SCREEN_HEIGHT

        elif self.center_y > SCREEN_HEIGHT:
            self.center_y = 0


        if self.center_x < 0:
            self.center_x=SCREEN_WIDTH

        elif self.center_x > SCREEN_WIDTH:
            self.center_x = 0





class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height = 16
        self.color = arcade.color.RED
        self.r = 8
        self.center_x=random.randint(0,SCREEN_WIDTH)
        self.center_y=random.randint(0,SCREEN_HEIGHT)
    

    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)




class Poop(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height = 16
        self.color = arcade.color.DARK_BROWN
        self.r = 8
        self.center_x=random.randint(0,SCREEN_WIDTH)
        self.center_y=random.randint(0,SCREEN_HEIGHT)
    

    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)

class Pear (arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height = 16
        self.color = arcade.color.GREEN_YELLOW
        self.r = 8
        self.center_x=random.randint(0,SCREEN_WIDTH)
        self.center_y=random.randint(0,SCREEN_HEIGHT)
    

    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, title="Snake Game!")
        arcade.set_background_color(arcade.color.BABY_POWDER)
        self.snake = Snake()
        self.apple = Apple()
        self.poop = Poop()
        self.pear = Pear()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Press Enter to start the game", 150,480,  arcade.color.BLACK, font_size=10)
        
        self.snake.draw()
        self.apple.draw()
        self.poop.draw()
        self.pear.draw()
        arcade.draw_text(f"Score: {self.snake.score}",start_x= 10, start_y= 10 ,color=arcade.color.BLACK_OLIVE,font_size = 10)
        #if (self.snake.center_x==0 or self.snake.center_x==SCREEN_WIDTH) or (self.snake.center_y==0) or (self.snake.center_y==SCREEN_HEIGHT):
            #self.back()

        if self.snake.center_x <= 0 or self.snake.center_x >= SCREEN_WIDTH or self.snake.center_y <= 0 or self.snake.center_y >= SCREEN_HEIGHT  or self.snake.score < 0 or self.snake.score<=-1:
            #arcade.draw_text('!!GAME OVER!!', start_x= 30, start_y= 250,color= arcade.color.BLACK, font_size = 45)
            self.back()
    #منطق کل بازی در این تابع
    def on_update(self, delta_time: float):
       self.snake.move() 
    

       if arcade.check_for_collision(self.snake , self.apple):
           self.snake.eat()
           self.apple=Apple()

       elif arcade.check_for_collision(self.snake , self.poop):
           self.poop=Poop()
           self.snake.score -=1

       elif arcade.check_for_collision(self.snake , self.pear):
           self.pear=Pear()
           self.snake.score +=2

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.ENTER:
            self.Search_move()

    def back(self):         
        if self.snake.center_x==0 :
            self.snake.change_x = 1
            self.snake.move()
            self.Search_move()

        elif self.snake.center_x==SCREEN_WIDTH:            
            self.snake.change_x = -1
            self.snake.move()
            self.Search_move()

        if self.snake.center_y==0:
            self.snake.change_y = 1
            self.snake.move()
            self.Search_move()

        elif self.snake.center_y==SCREEN_HEIGHT:
            self.snake.change_y = -1
            self.snake.move()
            self.Search_move()

    
    def Search_move(self):
        
        while self.apple.center_x >= self.snake.center_x:
            self.snake.change_x = 1
            self.snake.change_y = 0
            self.snake.move()
            
            if self.apple.center_y > self.snake.center_y:
                self.snake.change_y = 1
                self.snake.change_x = 0
                self.snake.move()

            elif self.apple.center_y < self.snake.center_y:
                self.snake.change_y = -1
                self.snake.change_x = 0
                self.snake.move()

        while self.apple.center_x <= self.snake.center_x:
            self.snake.change_x = -1
            self.snake.change_y = 0
            self.snake.move()
            
            if self.apple.center_y > self.snake.center_y:
                self.snake.change_y = 1
                self.snake.change_x = 0
                self.snake.move()
            
            elif self.apple.center_y < self.snake.center_y:
                self.snake.change_y = -1
                self.snake.change_x = 0
                self.snake.move()





my_game=Game()
arcade.run()
    