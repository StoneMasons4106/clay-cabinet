# ClayCabinet

This project is meant to provide an online store for the small local business, ClayCabinet.

ClayCabinet is a small singularly owned clay crafting business based in Kenmore, NY. This project gives ClayCabinet an online platform to advertise their products, and for customers to purchase them, create accounts, edit delivery information, and provide quick contact with the business owner.

[Feel free to view the live project here](https://www.claycabinet.com)!


## UX

This site is designed to give the user a visually pleasing way to browse products for the ClayCabinet online store. It caters to the customer base through the colorful and cute feel of the site.

For inspiration, I looked at a number of [Bootstrap Templates](https://bootstrapmade.com/) to get a beautiful front end design. In the end, I settled on using the [My Portfolio](https://bootstrapmade.com/myportfolio-bootstrap-portfolio-website-template/) template.


## Features

* **User Registration** - Allows user to store their delivery information, their default email, name, phone number, and view their order history.

* **SSO** - Allauth supports signing in and creating an account through many providers, I implemented and Facebook sign in and registration.

* **Contact Page** - Allows end users to send emails and questions to the store owner for easy correspondence.

* **Cart Model** - Allows users that are registered with the site to have their cart data stored for easy access if they leave the site and log back in.

* **Responsiveness** - Site responds to all device sizes and looks natural on Desktop, Mobile, and Tablet views.

* **Customizable Store** - Flexible product design allows the owner to add products, edit products, and delete them as their store changes.

* **Checkout** - Integration with Stripe allows people to shop and buy products, complete with confirmation emails for both the consumer, and the store owner.

* **Hubspot CRM Integration** - Filling out the contact form or buying something from the shop will either create a new contact in Hubspot, or update an existing one. Buying something will create a new deal with the details inside, and associate it to the proper contact.

* **Live Youtube Feed** - The home page contains the newest videos/shorts that have been posted on ClayCabinet's channel and is updated daily.

* **Contact Blacklisting** - In the interest of avoiding bots spamming contact forms, a blacklist was created on the back end to check by name or email. If there is a match, no contact is created in Hubspot and no email is sent.


## Technologies Used

**Languages Used**

* HTML5
* CSS3
* JavaScript
* Python
* Jinja


**Frameworks, Libraries & Programs Used**

1. [Bootstrap 5.1.3](https://getbootstrap.com/)
    * Bootstrap was used to assist with the responsiveness and styling of the website.

2. [Font Awesome](https://fontawesome.com/)
    * Font Awesome was used on most pages throughout the website to add icons for aesthetic purposes.

3. [Git](https://git-scm.com/)
    * Git was used for version control by utilizing VS Code to commit to Git and Push to GitHub.

4. [GitHub](https://github.com/)
    * GitHub is used to store the project's code after being pushed from Git.

5. [JQuery](https://jquery.com/)
    * JQuery was used to write shorter, simpler Javascript.

6. [Hover.css](https://ianlunn.github.io/Hover/)
    * Hover.css is used to change the text and background color of buttons and links upon hovering over them.

7. [Django](https://www.djangoproject.com/)
    * Django is the Python framework that this project was built on.

8. [Allauth](https://django-allauth.readthedocs.io/en/latest/)
    * Allauth is used for the authentication models, and SSO for this project.

9. [Postgres SQL](https://www.postgresql.org/)
    * Django uses a relational database system by default, and Heroku has a free Postgres extension to add on to any app.

10. [Django-Recaptcha](https://pypi.org/project/django-recaptcha/)
    * This allows for easy implementation of recaptcha used in the contact app.

11. [Django-Serverless-Cron](https://django-serverless-cron.readthedocs.io/en/latest/readme.html)
    * This allows for daily querying of the Youtube API and storing the response to display on the home page, rather than having to request a rate limit increase and possibly incurring extra cost.


### Known Bugs

* Upon the owner adding an apostrophe to a description in a new video or short on YouTube, the JSON response does not parse correctly in Javascript, and no videos render to the home page.
    * This is easily avoidable by not adding apostrophes or avoiding conjunctions like 'it is' versus it's.
* If the cart or order page has no orders/items, sometimes the footer takes on the background of the body of the page.
    * This is fixed on page reload and can not be consistently replicated for fixing at this time.