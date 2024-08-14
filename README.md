# Amigo Blog App

## Introduction

**Amigo Blog** is a Django-powered application designed to provide a platform for the Latin community in the UK to share their stories, experiences, and connect with others. Whether you are studying, working, or just visiting the UK, Amigo Blog allows you to create a profile, post your stories, and comment on others' posts, fostering a sense of community among Latin Americans in the UK.

<img width="1131" alt="Screenshot 2024-08-14 at 15 03 30" src="https://github.com/user-attachments/assets/0fa20c3c-9dd4-45b3-af3a-43b8f1023d23">

## Features

- **CRUD Functionality**: 
  - **Create**: Users can create posts to share their stories.
  - **Read**: Browse and read posts created by other users.
  - **Update**: Users can edit their own posts if they want to make changes.
  - **Delete**: Users have the ability to delete their own posts if needed.

- **User Profiles**: 
  - Create and customize your own profile.
  - Upload a profile picture.
  - View other users' profiles.

- **Comment System**:
  - Leave comments on posts to engage in discussions.
  - View and manage comments on your own posts.

- **Sidebar**: 
  - Displays the 5 most commented posts for easy access.

- **Footer**: 
  - Includes sections for Home, Contact, Admin (for admin users), and About.

#### Features Walkthrough

![Features Screenshot](https://github.com/user-attachments/assets/7cd35eaf-9387-4755-9708-f9ac63668e03)

![Features Screenshot](https://github.com/user-attachments/assets/0d0ae931-65a4-45d1-b5be-d5ea9bf82617)

#### Post Creating & User Update

![Post Creating & User Update Screenshot](https://github.com/user-attachments/assets/907b2cf9-343e-4faa-a1f6-35b352460f65)

## Persona & User Stories

### Target Audience

The Amigo Blog is designed for the Latin community in the UK, particularly targeting individuals between the ages of 16 and 38. This includes students, professionals, and visitors who want to connect with others, share their experiences, and learn from the stories of their peers.

### User Stories

1. **As a user, I want to create a profile so that I can share my personal details and stories with the community.**
2. **As a user, I want to post stories on the blog so that I can share my experiences in the UK with others.**
3. **As a user, I want to view other users' posts so that I can read about their experiences.**
4. **As a user, I want to edit my posts so that I can update or correct the information I have shared.**
5. **As a user, I want to delete my posts if I no longer want them visible on the blog.**
6. **As a user, I want to comment on other users' posts so that I can engage in discussions and share my thoughts.**
7. **As a user, I want to view and manage comments on my posts to control the discussion on my content.**

## UX Design

The design of Amigo Blog was guided by user experience (UX) best practices and created using wireframe tools. Research was conducted using marketing tools like HubSpot and SEMrush to understand user behavior and preferences, ensuring that the app meets the needs and expectations of its target audience.

### Wireframes

Wireframes were used during the planning phase to map out the layout of the app and the user journey. This process helped in visualizing the design and ensuring that the app would be intuitive and user-friendly.

![Wireframes](https://github.com/user-attachments/assets/9ad03b80-c60e-4a2a-809f-0aca8fe523b3)
![Wireframes](https://github.com/user-attachments/assets/33a7e5da-8d55-479a-8ba7-c90e73f6d7b4)


## Workflow

### Agile Methodology

For this project, I adopted an Agile methodology. This is the first time I have used this approach on a solo project, although I have used it as a group during hackathons. I feel this has helped me to:
- **Organize and prioritize my workflow**: This has been essential due to the very limited timeframe we had to complete this project.
- **Adjust my expectations and still produce the required MVP**: The iterative process allowed me to adapt and ensure that the most crucial features were delivered on time.

I created a site map and workflow diagram:

![Site Map](https://github.com/users/juanchitopimo/projects/4)
![Workflow Diagram](https://github.com/users/juanchitopimo/projects/4)
![Board](https://github.com/user-attachments/assets/6cfd4794-22d8-4da5-9c4d-a697ba4b6354)

I used GitHub Projects to convert my user stories into actionable tasks. The acceptance criteria were very helpful to ensure all necessary tasks were completed.

![Board](https://github.com/user-attachments/assets/6cfd4794-22d8-4da5-9c4d-a697ba4b6354)

### Models

In Amigo Blog, I used Django's built-in User Model and created custom models for posts and notifications. Here are the key models and fields used:

#### Post Model

| Name          | Type           | Key  |
|---------------|----------------|------|
| title         | CharField      |      |
| content       | TextField      |      |
| date_posted   | DateTimeField  |      |
| author        | ForeignKey     | FK   |
| excerpt       | TextField      |      |

#### Notification Model

| Name      | Type           | Key  |
|-----------|----------------|------|
| user      | ForeignKey     | FK   |
| message   | CharField      |      |
| timestamp | DateTimeField  |      |
| read      | BooleanField   |      |

## Testing

### CSS Validation

![CSS Validation](https://github.com/user-attachments/assets/30698db0-861b-4cfe-9ddf-d04306e00f7c)

### HTML Validation

#### Apart from the Django extension, the HTML has no issues.

![HTML Validation](https://github.com/user-attachments/assets/3d40ba3b-8c83-465d-a4dd-93c981a0c716)

### Python Validation

![Python Validation](https://github.com/user-attachments/assets/19d794e1-9cfe-4b9d-93e1-690b47f40c9a)
![Python Validation](https://github.com/user-attachments/assets/1e6a40a3-0d8b-4c84-8db0-7208866a7db4)
![Python Validation](https://github.com/user-attachments/assets/402462d1-905b-484a-b6f0-8451cb2505d6)
![Python Validation](https://github.com/user-attachments/assets/b514d285-0a84-4c3f-971e-4e4b921ca5f1)

### Functional Testing

![Functional Testing](https://github.com/user-attachments/assets/d53c767b-20ae-4ccc-8ac1-897c80f12358)

- **Profile Creation**: Tested the ability to create, view, and update profiles.
- **Post Creation and Management**: Verified that users can create, edit, and delete posts without issues.
- **Commenting**: Ensured that comments can be added, viewed, and managed on posts.
- **User Authentication**: Tested the registration, login, and logout processes to ensure security and usability.
- **Responsiveness**: Verified that the app is responsive and works across different devices and screen sizes.

### Performance Testing

- **Page Load Time**: Ensured that the blog pages load quickly even with multiple posts and comments.
- **Database Efficiency**: Checked the database queries to ensure they are optimized for performance.

### Cross-Browser Testing

- The app was tested across multiple browsers (Chrome, Firefox, Safari) to ensure compatibility.

## Responsiveness

The Amigo Blog app has been designed with a mobile-first approach to ensure a seamless experience across all devices. The layout and functionality have been tested on various screen sizes, including mobile phones, tablets, and desktop computers. No issues were encountered during testing, and the app's design adapts smoothly to different resolutions and orientations. Users can access the blog, create and manage posts, and interact with the community with ease, regardless of the device they are using.


## Bugs & Improvements

- On the edit recipe page, there is no success message appearing. It does reload the page if successful and returns to the top of the page.
- The only feature not currently working is the 'forgot your password' link; email authentication was out of scope for this project.
- **Layout Responsiveness**: In some sizes, the layout responsiveness is not perfect, leading to design inconsistencies across different devices.
- **Blog Post Editing**: The blog post editing options are limited. There is also an issue related to finding a valid digest in the 'integrity' attribute, which may affect certain security checks.
- **Hero Image and Message**: The hero image and message could be improved for better visual appeal and user engagement.

## Technologies Used

- **CSS**: For styling and layout of the app.
- **Django**: The main framework used for developing the app.
- **HTML**: Markup language used to structure the app's pages.
- **Bootstrap**: Used to ensure responsive and modern design, particularly with forms and layout.
- **Python**: The programming language used for server-side logic.
- **ElephantSQL Postgres Database**: Used as the database for storing user information, posts, and comments.
- **Crispy Forms**: Utilized to create elegant, responsive forms with minimal effort, ensuring that form layouts are consistent and visually appealing.
- **GitPod**: The development environment used for coding and testing the app.
- **GitHub**: Used for version control and code hosting, ensuring that the project is tracked and managed effectively.
- **GitHub Projects**: Employed for implementing Agile Methodology, tracking tasks, and managing workflow.
- **Wireframes**: Created to plan the user interface and experience of the app.
- **SEMrush and HubSpot**: Utilized for marketing research and strategy development to better understand user needs and behavior.

  
## Deployment

### Deployment to Heroku

<img width="831" alt="Screenshot 2024-08-14 at 14 01 21" src="https://github.com/user-attachments/assets/1a37edc7-65af-40bb-80dc-d6ab2685dfe7">

To successfully deploy the Amigo Blog to Heroku, follow these steps:

1. **Create a Heroku Account**: If you don’t have one, create an account at [Heroku](https://www.heroku.com/).

2. **Install Heroku CLI**: Install the Heroku Command Line Interface (CLI) to manage your app from the terminal. You can download it from [here](https://devcenter.heroku.com/articles/heroku-cli).

3. **Create a Heroku App**: 
   - Run `heroku create your-app-name` in your terminal. 
   - This will create a new Heroku app and add a Git remote called `heroku`.

4. **Prepare the Django Project**:
   - Ensure your `requirements.txt` and `Procfile` are correctly configured. The `Procfile` should contain:
     ```
     web: gunicorn your_project_name.wsgi --log-file -
     ```

   - Make sure your `settings.py` is configured for production, including setting `DEBUG` to `False` and configuring the allowed hosts.

5. **Set Up the Database**:
   - Add the `dj_database_url` package to your `requirements.txt`.
   - Configure the `DATABASES` setting in `settings.py` to use the Heroku Postgres database.

6. **Push to Heroku**:
   - Commit your changes and push them to Heroku using:
     ```
     git push heroku main
     ```
   - Heroku will automatically build and deploy your app.

7. **Run Migrations**:
   - After deployment, run the migrations to set up your database:
     ```
     heroku run python manage.py migrate
     ```

8. **Create a Superuser**:
   - To access the Django admin, create a superuser:
     ```
     heroku run python manage.py createsuperuser
     ```

9. **Open Your App**:
   - Finally, open your app in the browser:
     ```
     heroku open
     ```

Your Django app should now be live on Heroku.

## Credits

- The structure of my website was based on the tutorial from @desphixs: https://www.youtube.com/@desphixs
- This project was also based on the walkthrough project of the Code Institute.
- **ChatGPT** was used for troubleshooting, bug fixing, and content generation.
- Thanks to the other members of the **Bootcamp** for their technical and moral support.
- **Font Awesome** was used for icons.
- **Google Fonts** was used for typography.
- **Wireframes** were created using **Balsamiq**.
- **Logo** and **flow chart** created using **Canva**.
- **Canva** was also used for picture editing.
- **HubSpot** was used for marketing research.
- **YouTube** was used for research and further learning.
- Thanks to the **Code Institute** team for their guidance and support.
- **Pixabay** was used for image research.
