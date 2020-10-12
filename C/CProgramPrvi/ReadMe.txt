"\t" is for tab; 
"\n" is for new line; 
"\a"(alarm) is for a sound; 
These things must go between quotation marks;
When we want to make a variable first we need to type in what our variable is going to be (a word, number,...); 
We can do this by typing in some text; 
For a whole number it is "int"; 
When we write int we need to define a name of that variable with letters; 
We can't start name of the variable with "space, underscore or with a weird character"; 
After naming the variable we can define it with a single number or with some kind of mathematical problem to make computer to calculate it; 
After that, we use "printf" to use a variable; 
We put that variable in the text with %d; 
We should not forget that we need to put the name of the variable after text that we want to print out, we should divide this with a colon and a space after colon and all this must be after quotation marks; 
example: 
	int age; 
	age=15 or 2018-2003; 
	printf("Mario is %d years old!\n", age);
	return 0;
There is one extra special simbol that is \o this means end of a line;
Back to variables if we want to make a variable that is going to contain some characters first we need to tell C that we want to make a variable with letters;
We are going to do that with "char" function;
After we name that variable we put [] these brackets and inside we put how many bytes is that information containing;
One letter is one byte, space is also one byte;
At the end we need to put \o which is conteining one byte;
When we want to name a place where our variable is going to be we use it by putting "%s";
example: 
	char name [16] = "Mario Jovanovic";
	printf("My name is %s.\n", name);
	return 0;
You can put after the value of variable name;
example: 
	char name [16]
	name = "Mario Jovanovic";
	printf("My name is %s.\n", name);
	return 0;
It is not very important to put the number of characters in brackets, but always try to put it.
If we don't put the right number in brackets at the end of our sentence number 7 will appear;
In our variable "name" Mario Jovanovic;
M is postion number 0;
A is position number 1;
R is position number 2 and so on;
When we want to change a character in our variable first we need to put a name of a variable thet we are working with;
After that we need to name a character with a position number in [] these brackets;
Next we write between single quotes "'" what letter are we changing it into;
Then we just print info that we want to;
example:
	name [2] = 'k';
	printf("My name is %s.\n", name);
	return 0;
We ue "strcpy" to change variable;
example:
	strcpy(food, "beacon");	
	printf("I love %s.\n", food);
	return 0;
We use printf to print information on the screen and we use scanf to get information from the user;
example:
	printf("What is your name?\n");
        scanf("%s", firstName);
        printf("What is yours crush name?\n");
        scanf("%s", crush);
        printf("How many houses will you have?\n");
        scanf("%d", &numberOfHouses);
        printf("Your name is %s. Yours crush name is %s. You will Have %d houses.\n", firstName, crush, numberOfHouses);
"%f" is used to print float;
We use float when we want decimal places and it is always better to use float than integer because we will get correct solution;
With an integer we would get solution without decimal places because integers can only be whole numbers;
Instead writing values to all variables, if they are the same we can just write"a = b = c = 100";
When we use variables and don't use them in array we need to add in front of a variable "&" sign;





















