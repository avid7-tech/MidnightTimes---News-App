# The Midnight Times

## Table of Contents

1.  [Introduction](#introduction)
2.  [Features](#features)
3.  [Visuals](#Visuals)
4.  [Installation](#installation)
5.  [Configuration](#configuration)
6.  [Usage](#usage)
7.  [Directory Structure](#directory-structure)
8.  [Models](#models)
9.  [Forms](#forms)
10. [Views](#views)
11. [URL Configuration](#url-configuration)

## Introduction

The Midnight Times is a customer-facing web-based application allows users to search for news articles using the News API and view results of previous searches. Users can register, log in, and manage their keywords. Superusers have additional control panel functionalities to manage users and view trending keywords.

## Features

- User authentication and registration
- Keyword search with various filters based upon language, category and date
- Search results caching
- User-specific search history
- Keyword management
- Superuser control panel
- Notes Management for students and Assiduous readers

## Visuals

### Home Page

Search results for Ronaldo and Arab language
![The Midnight Times - Google Chrome 03-07-2024 10_54_35](https://github.com/avid7-tech/MidnightTimes---News-App/assets/76569713/e70f6b9a-2198-4b51-ab09-5dd9e07bb44c)


### Registration Form
![The Midnight Times - Google Chrome 03-07-2024 11_01_11](https://github.com/avid7-tech/MidnightTimes---News-App/assets/76569713/3cba3104-6600-4b30-9ea8-781b749e7333)


### Login Form
![login form](https://github.com/avid7-tech/MidnightTimes---News-App/assets/76569713/a1a558f1-da60-471d-9d2d-f84ab3555db0)


### Admin Panel
![admin panel](https://github.com/avid7-tech/MidnightTimes---News-App/assets/76569713/a2a89037-fdc7-439c-9fa7-3684da114106)


### Trending Keyword
![trending keywords](https://github.com/avid7-tech/MidnightTimes---News-App/assets/76569713/9f21a5b3-5f1c-4bf6-81d3-97352ea0757a)


## Installation

1.  Clone the repository:

```
git clone https://github.com/avid7-tech/MidnightTimes---News-App
```

2.  Change to the project directory:

```
cd news_app
```

3.  Setup the virtual environment:

```
py -m venv .venv
.venv/bin/activate
```

4.  Install the dependencies:

```
pip install -r requirements.txt
```

## Configuration

1.  Create a `.env` file in the project root and add your News API key:

```
NEWS_API_KEY=your_news_api_key
```

2.  Apply migrations:

```
python manage.py migrate
```

3.  Create a superuser:

```
python manage.py createsuperuser
```

4.  Run the development server:

```
python manage.py runserver
```

## Usage

1.  Register a new user or log in with an existing account.
2.  Add keywords and search for news articles.
3.  View and manage your search history.
4.  Add Notes for reference
5.  Superusers can access the control panel to manage users and view trending keywords.

## Models

- `Keyword`: Represents a keyword associated with a user.
- `SearchHistory`: Represents a search history entry for a keyword and it's result search by a user.

## Forms

- `KeywordForm`: Form for creating and updating keywords.
- `UserRegistrationForm`: Form for registering a new user.

## Views

- `home`: Handles news search and displays results.
- `search_history`: Displays user's search history.
- `register`: Manages user registration.
- `keyword_list`: Lists keywords added by the user.
- `keyword_create`: Handles keyword creation.
- `keyword_delete`: Handles keyword deletion.
- `block_user`: Blocks/unblocks a user.
- `set_limit`: Sets keyword limit for a user.
- `not_authorized`: Displays not authorized message for non-superusers.
- `signin`: Handles user sign-in.
- `control`: Superuser control panel with user management and trending keywords.

## URL Configuration

Maps URLs to views, defining the routes for various functionalities:

```
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('create/', views.keyword_create, name='keyword_create'),
    path('<int:keyword_id>/delete/', views.keyword_delete, name='keyword_delete'),
    path('list/', views.keyword_list, name='keyword_list'),
    path('control/', views.control, name='control'),
    path('control/block/<int:user_id>/', views.block_user, name='block_user'),
    path('control/set_limit/<int:user_id>/', views.set_limit, name='set_limit'),
    path('login/', views.signin, name='signin'),
    path('not_authorized/', views.not_authorized, name='not_authorized'),
    path('search-history/', views.search_history, name='search_history'),
]
```
## Duration
I spent a total of approximately 33+ hours working on this project. The time was allocated across various phases as follows:

1.  **Learning Django**:
    
    -   Time: 10 hours
    -   Activities: As I was new to Django, I first went through the official documentation and several tutorials to understand the framework and its components.
2.  **Initial Planning and Setup**:
    
    -   Time: 1.5 hours
    -   Activities: Project planning, setting up the development environment, and configuring Django.
3.  **Model and Database Design**:
    
    -   Time: 3 hours
    -   Activities: Designing models for `Keyword` and `SearchHistory`, setting up SQLite database, and creating migrations.
4.  **User Authentication and Registration**:
    
    -   Time: 2 hours
    -   Activities: Implementing user registration, login, and authentication features.
5.  **Keyword Management**:
    
    -   Time: 1.5 hours
    -   Activities: Developing views and forms for creating, listing, and deleting keywords.
6.  **News Search Integration**:
    
    -   Time: 6 hours
    -   Activities: Integrating News API, implementing search functionality with filters, and setting up caching.
7.  **Search History Feature**:
    
    -   Time: 1.5 hours
    -   Activities: Creating the search history view, storing search results, and displaying history to users.
8.  **Control Panel for Superusers**:
    
    -   Time: 3 hours
    -   Activities: Developing the control panel, managing user blocks, and trending keyword integration
9.  **Frontend Development**:
    
    -   Time: 2 hours
    -   Activities: Designing and coding templates using Bootstrap and tailwind CSS for a user-friendly interface.
11.  **Documentation**:
    
    -   Time: 2 hours
    -   Activities: Writing project docstring, README file.
## Experience
Since I was new to Django, I invested significant time in learning the framework through the documentation and tutorials. This helped me how to use the Django "Ridiculously fast" as give in official documentation.

Project helped me in thinking critically, using various logics to make something happen and at the same time not to obstruct other components in app.

Caching the user results, and also storing them locally helped me appreciate the importance of optimizing application performance and reducing load times.

Breaking down project into manageable phases and setting clear goals helped in efficient management.

Making sure easy and user-friendly control for user was also an important part.

Achieving the major milestones as per the given instructions feels incredibly satisfying and gives a strong sense of accomplishment.

Thanks a lot for the opportunity!
