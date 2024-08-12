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

The development of Amigo Blog followed the **Agile Methodology**, which allowed for iterative progress and flexibility. The project was managed using GitHub Projects, where tasks were organized and tracked. Key tools and processes used in the workflow included:

- **Django User Models**: To manage user profiles and authentication.
- **Wireframes**: To plan the user interface and experience.
- **Pen and Paper**: For initial brainstorming and sketching ideas.

## Testing

### Functional Testing

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

### Security Testing

- **CSRF Protection**: Ensured that forms are protected against Cross-Site Request Forgery.
- **User Authentication**: Verified that user data is secure and authentication is handled properly.

## Future Enhancements

- **Notifications**: Implement a notification system to alert users of new comments on their posts.
- **Search Functionality**: Add a search bar to allow users to search for posts by keywords.
- **Social Media Integration**: Allow users to share their posts on social media platforms.

## License

This project is licensed under the MIT License.
