## BOOM E-commerce
BOOM is an e-commerce specialized in sports clothes and workout light equipment such as resistance bands, yoga balls, dumbbells, and many others.

BOOM is targeting both women and men of all ages and sizes. We want to cultivate equality, integration and build a new health and well being community. 

Be healthy and happy is crucial for human development, for that reason we want to provide a platform where our clients can purchase comfortable and high-quality products while experiencing a smooth and easy purchase process.

The deployed version in Heroku: [View](https://boom-ecommerce.herokuapp.com/).

## UX
Boom is a user friendly, responsive, and simple platform for purchase sports clothes and complements.

A user will be able to:
- Register an account. 
- Login to personal account to proceed to checkout.
- Search by keywords for any product
- Filter the products by category and price
- View detail product description
- Add products to the cart
- View and modify cart
- Go through a sophisticated and secure checkout process with Stripe API.
- Contact us through email contact form.
- See success messages after login/out, register, adding products to cart.
- See warning messages if the user wants to proceed to checkout with cart empty.
- Navigate smoothly throughout the website.

Administrators will be able to:
Login to Django dashboard to:
- Create products
- Improve/manage easily products
- Get information about customers
- Handle orders
- Edit customer information.

#### The wireframe of BOOM: [Bring me there.](https://drive.google.com/drive/folders/1rpNlFLjGv-LZ2yA9FIYGAiPl0j3XWSdf?usp=sharing) 

## Features
### Global Features
- Responsive Navbar with logotype, search bar, categories dropdown, and user icons such as login, cart, profile. In smaller screens, all the features unless the Logo, are wrapped in a hamburger icon.
- The Search bar displays the results on the search view.
- Cart icon displays amount of items in cart.
Footer with another version of the logo and links to social accounts, blog, FAQ, and Contact Us.

#### Home page
In this page a motivating gif is displayed at the beginning of the page, followed by the 3 images that link with the specified product category.
A "new arrivals" section with only 4 products,  "Deal of the week" which is a simple product image that can be customized by id and finally an offer section with links to (future) student discounts, Swedish payment option, and (future) workout app.

#### Products page
Main Product list page. This page lists all products available. Each product has an image, price and name linked to the detail view of the item. The same template is reused to display products depending on the category selected. On the left side of the page, filters by price and categories can be found.

#### Product detail page
On this page, the product image is displayed bigger, user can see the name, description, price, and a quantity form which automatically stats in 1. When a user click add to cart, will be redirected to all products view (To impulse more purchases) and a success message will be displayed notifying that the cart has been updated.

#### Search Page
This page follows the same structure of the "products page". The user is redirected to there where relevant results are displayed.

#### Cart
Users can access their cart by clicking the cart icon. There a clean table with image, product name, quantity, price, subtotal, delete product and total amount to pay are in place.
The quantity can be modified directly by clicking in + or - icons. If the quantity is reduced to 0, then the product will be automatically deleted from the cart, deducting its value from the total amount to pay.
Two buttons are provided to either go back shopping that link to "products page" or proceed to checkout.
Price is automatically calculated after add, edit or remove items.

#### Checkout
Users can access the checkout functionality by clicking the button "proceed to checkout" in cart. If the user is not logged In, will be redirected to the login page, with an aim of recording customer information. Otherwise will be connected to the Stripe's API, where the shopping list with the products name, quantity, and price can be seen.

If the user has to login, items will persist in cart after successful login.
If payment is processed, the user is redirected to payment_success page.
#### Contact Us
Simple and clean page with contact information, a contact form for questions, feedback, or partnership purposes.
Finally, a Google Maps API is in place with the coordinates of our "central office" in Sweden.

### Features Left to Implement
- Include size and color tags to products for more specialized service.
- Develop an order/delivery system, which I believe is crucial for e-commerce.
- Build partnership with other firms to provide student or other discounts.
- Enable discount feature in the checkout stage.
- Build a Blog connected with user accounts, so they can share knowledge, experiences about health and training, and also to rate our products.
- Create rating functionality
- Recommendation/rating engine for displaying popular and frequently bought items.
- Sort products by date to create an automated engine for displaying new releases.
- Create a wish list feature that can be shared.
- Create a workout app as a complement for a rich experience.
- Include more pictures per product.
- Include a stock level to know how many have been sold and when a new order needs to be placed to maintain a safety stock.
-Tests

## Technologies Used
Technologies Used
- Gitpod
- HTML
- CSS
- Bootstrap
- Font awesome
- JavaScript
- Python
- Django
- Stripe
- GitHub
- Heroku
- AWS S3
- Travis
- SQLite

## Testing
| Test case | Descripción | Result |
| --- | --- | --- |
| `--` | Home Page | -- |
| `1` | Click into all the links that will redirect to its specific page. Such as Logo, Categories, Blog, FAQ, Contact Us, shop now, student discount, Klarna, home workout app, social icons. | passed |
| `2` | Click into every product to see detail view of it.| passed |
| `3` | Search a product by a keyword return to search page with relevant results| passed |
| `4` | Click into user icon redirect to login if user is logged out and to profile if is logged in| passed |
| `5` | Click into cart icon redirect to cart.html either empty of with items| passed |
| `6` | Search a product by a keyword return to search page with relevant results| passed |
| `--` | Products page | -- |
| `7` | Select each category and only product associated with that category appears | passed |
| `8` | Change price range and products only in that price range appears| passed |
| `9` |Choose to order the products by name, price or default| passed |
| `10` | Search a product by a keyword return to search page with relevant results| passed |
| `--` | Detail page | -- |
| `11` |When choosing quantity = 0 or lower an error of "You should add at least 1 unit" appears.  | passed |
| `12` |Choose a quantity > 0, the product is added to the cart with the quantity specified. A message appears to notify successful append and returns to all products page | passed |
| `--` | Cart | -- |
| `13` |When Increasing or decreasing quantity both the subtotal and total change amount| passed |
| `14` |When increasing or decreasing quantity of one product, the others remain unchanged | passed |
| `15` |Click into "proceed to checkout" with an empty cart retrieve a message of "Your cart is empty, go shopping!" and redirect to again | passed |
| `16` |Click into "go back shopping" redirect to all products page but keep cart session| passed |
| `--` | Checkout | -- |
| `17` |Click to "proceed to checkout" with cart items connects with Stripe API successfully| passed |
| `18` |click into "go back" during payment process returns to all products page| passed |
| `19` |If payment is successful, redirect to "thankyou.html" | passed |
| `--` | Contact Us| -- |
| `20` |Send an empty form return an error message in the field | passed |
| `21` |write a wrong email format return an error message in the field | passed |
| `--` | Login & Register | -- |
| `22` |try to login with a new user, return message.error | passed |
| `23` |click to forgot password redirect to reset password view  | passed |
| `24` |login with existing user credential, return a success message and redirect to home page | passed |
| `25` |try to register a new user, returns a success message, the user is created and is redirected to home page | passed |

### Deployment

#### For local deployment:
Create a new GitHub repository.
Open it using Gitpod
Enter the following commands :
- git clone https://github.com/Dreeaml/Boom-ecommerce.git
- pip3 install -r requirements.txt
Create a .env file, enter and custome the following:
SECRET_KEY = "your own key" # Django app secret key
AWS_ACCESS_KEY_ID = "your own key" # Amazon S3
AWS_SECRET_ACCESS_KEY = "your own key" # Amazon S3
STRIPE_SECRET_KEY = "your own key" # Stripe
STRIPE_PUBLISHABLE_KEY = "your own key" # Stripe
DATABASE_URL = "your own key" # Postgres key from Heroku

In the terminal, enter the following commands :
```
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver
```

Make sure you have a .gitgnore file and .env is included there to not expose your secret variables.
 
### Heroku
Go to [Heroku](heroku.com), create an account and a new project.
In settings, click on config vars and add the already mentioned variables.
Additionally, go to deploy to connect the project with your Github repo.

In Gitpod, create a Procfile file and type the following code: 

``` web: gunicorn <proyect name>.wsgi:application ```

Then is time for your first deployment. Run:

``` 
git add .
git commit -m "your commit message"
 ```

After it is successfully deployed, go to Heroku, under deploy section, and click on "deploy branch".

## Credits

### Content
The product names, description, and other texts are from [Gymshark](https://se.gymshark.com/)

### Media
The photos and gifs used in this site were obtained from [Abode Stock](https://stock.adobe.com/fi/)

### Acknowledgements
I received inspiration for this project from [Gymshark](https://se.gymshark.com/), [SOXS](https://github.com/Code-Institute-Submissions/SOXS_Store), and other inspiring projects from [Code Institute](https://codeinstitute.net/).

The Styling of the webpage is customized from a (Colorlib](https://colorlib.com/) open-source template.
### Special thanks to
Code institute team, mentor, tutors, Slack community for helping me to tackle project issues.
