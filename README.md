# Amigo Blog App

## Introduction

**Amigo Blog** is a Django-powered application designed to provide a platform for the Latin community in the UK to share their stories, experiences, and connect with others. Whether you are studying, working, or just visiting the UK, Amigo Blog allows you to create a profile, post your stories, and comment on others' posts, fostering a sense of community among Latin Americans in the UK.

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

  <img width="1178" alt="Screenshot 2024-08-13 at 21 17 56" src="https://github.com/user-attachments/assets/7cd35eaf-9387-4755-9708-f9ac63668e03">

  <img width="1976" alt="Screenshot 2024-08-13 at 21 34 57" src="https://github.com/user-attachments/assets/0d0ae931-65a4-45d1-b5be-d5ea9bf82617">

#### Post Creating & User Update
  <img width="2522" alt="Screenshot 2024-08-13 at 21 49 38" src="https://github.com/user-attachments/assets/907b2cf9-343e-4faa-a1f6-35b352460f65">

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

<img width="1001" alt="wireframes" src="https://github.com/user-attachments/assets/9ad03b80-c60e-4a2a-809f-0aca8fe523b3">
<img width="389" alt="wireframes1" src="https://github.com/user-attachments/assets/33a7e5da-8d55-479a-8ba7-c90e73f6d7b4">

## Technologies Used

- **CSS**: For styling and layout of the app.
- **Django**: The main framework used for developing the app.
- **HTML**: Markup language used to structure the app's pages.
- **Bootstrap**: Used to ensure responsive and modern design, particularly with forms and layout.
- **Python**: The programming language used for server-side logic.
- **ElephantSQL Postgres Database**: Used as the database for storing user information, posts, and comments.
- **Cloudinary**: All user-submitted images are uploaded and managed through Cloudinary, providing reliable media hosting.
- **GitPod**: The development environment used for coding and testing the app.
- **GitHub**: Used for version control and code hosting, ensuring that the project is tracked and managed effectively.
- **GitHub Projects**: Employed for implementing Agile Methodology, tracking tasks, and managing workflow.
- **Wireframes**: Created to plan the user interface and experience of the app.
- **SEMrush and HubSpot**: Utilized for marketing research and strategy development to better understand user needs and behavior.

## Workflow

### Agile Methodology
For this project, I adopted an Agile methodology. This is the first time I have used this approach on a solo project, although I have used it as a group during hackathons. I feel this has helped me to:
- **Organize and prioritize my workflow**: This has been essential due to the very limited timeframe we had to complete this project.
- **Adjust my expectations and still produce the required MVP**: The iterative process allowed me to adapt and ensure that the most crucial features were delivered on time.

I created a site map and workflow diagram:

https://github.com/users/juanchitopimo/projects/4
![](vscode-remote://juanchitopi-amigoblogfi-e12nif7seaj.ws.codeinstitute-ide.net/workspace/Amigo-Blog-final/readme_images/board.png)

<img width="1129" alt="board1" src="https://github.com/user-attachments/assets/6cfd4794-22d8-4da5-9c4d-a697ba4b6354">


![Workflow Diagram](https://github.com/users/juanchitopimo/projects/4)

I used GitHub Projects to convert my user stories into actionable tasks. The acceptance criteria were very helpful to ensure all necessary tasks were completed.

![board](/workspace/Amigo-Blog-final/readme_images/board.png)

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
### main CSS Validation
<img width="876" alt="css_check" src="https://github.com/user-attachments/assets/30698db0-861b-4cfe-9ddf-d04306e00f7c">

### Main base HTML Validation

#### Appart for the Django extention the html has no issues.

<img width="1230" alt="Screenshot 2024-08-14 at 13 46 08" src="https://github.com/user-attachments/assets/3d40ba3b-8c83-465d-a4dd-93c981a0c716">

### Python Validation

<img width="962" alt="Screenshot 2024-08-14 at 12 50 02" src="https://github.com/user-attachments/assets/19d794e1-9cfe-4b9d-93e1-690b47f40c9a">
<img width="1113" alt="Screenshot 2024-08-14 at 12 47 07" src="https://github.com/user-attachments/assets/1e6a40a3-0d8b-4c84-8db0-7208866a7db4">
<img width="972" alt="Screenshot 2024-08-14 at 12 43 02" src="https://github.com/user-attachments/assets/402462d1-905b-484a-b6f0-8451cb2505d6">
<img width="979" alt="Screenshot 2024-08-14 at 12 33 13" src="https://github.com/user-attachments/assets/b514d285-0a84-4c3f-971e-4e4b921ca5f1">


### Functional Testing

<img width="793" alt="Screenshot 2024-08-14 at 12 51 41" src="https://github.com/user-attachments/assets/d53c767b-20ae-4ccc-8ac1-897c80f12358">

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

## Credits

- The structure of my website was based on this tutorial by Dee Mc: [YouTube Tutorial](https://www.youtube.com/watch?v=OBsLgCm-Ayo&t=509s)
- This project was also base on the walkthouproject of the Code Institute. 
- **ChatGPT** was used for troubleshooting, bug fixing and content generation. 
- Thanks to the other members of the **Bootcamp** for their technical and moral support.
- **Font Awesome** was used for icons.
- **Google Fonts** was used for typography.
- **Wireframes** created using **Balsamiq**.
- **Logo** and **flow chart** created using **Canva**.
- **Canva** was also used for picture editing.
- **HubSpot** was used for marketing research.
- **YouTube** was used for research and further learning.
- Thanks to the **Code Institute** team for their guidance and support.
- **Pixabay** was used for image research.

