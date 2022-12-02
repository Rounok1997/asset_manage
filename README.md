This app tracks the gadgets a company is giving to their representatives. The usefulness is as takes after: To begin with, you've got to enlist on the internet application on hehalf of a company. You have got to supply your company title with no spaces, company mail and a password for security parpose. The company title can be resolved with dashes or underscores (ex: The_drug_Company). After sigining in, you'll be able make a list of your accessible assets/gadgets/devices merely want to grant to your representatives. Let's say you want to supply tablets, portable phones and tablets to your representatives. So the accessible resource for you is Versatile phone, Tablet, and Laptop. You fair need to enter the sort of your accessible gadget. It'll consequently be spared to the database having a basic connect to your company. You'll too erase any resource sort on the off chance that you need. You'll be able alter the sort title as well.

At that point you've got another option to add your workers. You have got to supply an special ID for each of your representative. Beside the ID, You'll be able store their title as well. The employee list will be spared with a link to your company and no other person can see the list of your workers. This applies for the available assets as well. The final thing you'll do is , you'll be able allot resources to your workers. You'll relegate no gadget at all for any particular employee. Also you'll be able allot one or more than one gadget for each of them. You'll be able look workers by their ID and can see which or how numerous gadgets they have been given. You'll spare the issue date and return date for each task. Too you'll be able spare a log of the condition of gadgets. In which state gadget is given and in which state the gadget is returned. You'll too erase any occurrence in case you need.

For enlistment, login, and logout, the knox library has been utilized. It may be a third party library for django rest system to illuminate the confirmation and authorization prepare. It works on token based framework and you've got to pass your interesting token in conjunction with your ask on each move you make. The backend is made with django and utilized api system is django rest system. Django-filters is utilized to look workers within the "given resource" area. For testing reason, sqlite database is utilized in this venture.

#The available endpoints are:

/auth/login/

/auth/register/

/auth/logout/

/asset/

/asset/<int:pk>

/employee/

/employee/<int:pk>

/given_asset/

/given_asset/<int:pk>
