# Social-Space

#### Video Demo: <URL HERE>

#### Description:

This is my final project of CS50x:CS50's Introduction to Computer Science. Social Space is a web-based application platform that allows you to connect with people who share your interests. You can create a profile, join groups, and participate in discussions. Social Space is a great way to meet new people and make friends.

#### Features

- Profile creation
- Post creation
- Group creation
- Space's Discussion forum
- Space's group messaging
- Post management
- Space management

#### Technologies Used

Python, Flask, Flask-SocketIO, SQLite, SQL, HTML, CSS, Bootstrap, JavaScript, jQuery.

#### Clone The Project

```
$ git clone https://github.com/paing-myo-swe/social-space.git
```

#### Change directory to the Project

```
$ cd social-space
```

#### Enable a Virtual Environment

- Create .venv virtual environment
- Activate .venv

```
$ python3 -m venv .venv
```

```
$ . .venv/bin/activate
```

#### Install Require Packages

- Run pip3 install command to using requirements text

```
$ pip3 install -r requirements.txt
```

**If do you want to reinitialize database**

#### Database Initialization

- Run the init-db command to reinitialized the database.

```
$ flask --app app init-db
```

#### Run the Project

- To start project run flask run command

```
$ flask --app app run --debug
```

#### Get Started

- App is running on http://127.0.0.1:5000
- Go to the browser
- Enter http://127.0.0.1:5000 in url

#### Account Creation (Register)

- URL: http://127.0.0.1:5000/register
- Click "Register" button on navigation bar
- You will redirected to registration page
- You will see the registration form
- Enter username and password
- Username must be unique and at least 3 characters long
- Password must be at least 8 characters long
- If your username have already account you will see alert message "User {username} is already registered."
- If successed you were redirected to home page
- You will see alert message "User {username} is registered."

#### Account Login

- URL: http://127.0.0.1:5000/login
- If you have already an account you can login
- Click "Login" button on navigation bar or Sign In link on registration form
- You will redirected to login page
- You will see the login form
- Enter username and password of when you registered
- If successed you were redirected to home page
- You will see alert message "User {username} is logged in."

#### Home Page

- URL: http://127.0.0.1:5000/
- There is a tab named "Home" on navigation bar
- You will see a title "Posts"
- Home page is showing users created post lists by ordering DESC over created
- If there is no post yet you can create new post by clicking "New Post" button
- If you don't see "New Post" button, please login first
- In Post List, every post card shows
- Posted By username, Posted On Date Time, Post Title and Post Body
- If your own post, you will see "Edit" button to update
- If you click "Edit" button it will redirect to Post Edit Page

#### Post Create Page

- URL: http://127.0.0.1:5000/create
- You will see Post Form
- Enter Post title and Post Content
- After submitted it will redirect back to Home Page
- You will see alert message "Post created successfully."
- You will see you created post at the top

#### Post Edit Page

- URL: http://127.0.0.1:5000/{post-id}/update
- You will see Post Edit Form and "Delete" button
- Enter Post title and Post Content
- After submitted it will redirect back to Home Page
- You will see alert message "Post updated successfully."
- You will see you created post at the top
- If you click "Delete" button, you will see a confirmation dialog
- "Are you sure want to delete?"
- If you deleted you will see alert message "Post deleted successfully."
- After deleted it will redirect back to Home Page

#### Spaces

- URL: http://127.0.0.1:5000/spaces/
- There is a tab named "Spaces" on navigation bar
- You will see a title "Spaces"
- Spaces page is showing users created space lists by ordering DESC over created
- If there is no space yet you can create new space by clicking "New Space" button
- If you don't see "New Space" button, please login first
- In Space List, every space card shows
- Space Logo, Space Name and Space Description
- If your own space, you will see "View Details" button to view deatils
- If you click "View Details" button it will redirect to Space Details Page
- If you didn't joined yet, you will see "Join" button to join space
- If you click "Join" button, you will see a confirmation dialog
- "Are you sure to join this space?"
- If you joined you will see alert message "You have joined this space."
- After joined it will redirect to Space Details Page

#### Space Create Page

- URL: http://127.0.0.1:5000/spaces/create
- You will see Space Form
- Enter Space name and Space Description
- After submitted it will redirect back to Spaces List Page
- You will see alert message "Space created successfully."
- You will see you created space at the top

#### Space Details Page

- URL: http://127.0.0.1:5000/spaces/{space-id}
- You will see space logo and about of space description
- You will also see Space code, Space Admin, Space Created Date and Space Members List
- In Space Member List there is User Id, User Name and Joined Date are showing
- You will see "Leave" button and "Live Chat Room" button
- If you click "Leave" button, you will see confirmation dialog
- "Are you sure to leave?"
- If you leaved you will see alert message "You have left from this space."
- After leaved it will redirect to Spaces List Page
- If you are admin of space, you will see "Edit" button
- In members list table if you are admin of space, you will see "Remove" button
- You can remove user from this space

#### Space's Live Chat Room

- URL: http://127.0.0.1:5000/spaces/{space-id}/chat
- This is a realtime Live Chat Room
- If you click "Live Chat Room" button it will redirect to space's chat room
- You will see chat messages list and user activities (entered or left)
- You can send message to space's members
- You can leave from space's chat room
- If you leaved from space's chat room it will redirect back to Space Details Page

#### Profile Page

- URL http://127.0.0.1:5000/profile
- You will see your profile

#### About Page

- URL http://127.0.0.1:5000/about
- You will see about this project

#### Thanks

Finally I would like to say thank you David J. Malan and CS50's Team. **This was CS50x!**
