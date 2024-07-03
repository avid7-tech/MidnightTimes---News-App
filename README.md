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
10.  [Views](#views)
11.  [URL Configuration](#url-configuration)



## Introduction

The Midnight Times is a customer-facing web-based application allows users to search for news articles using the News API and view results of previous searches. Users can register, log in, and manage their keywords. Superusers have additional control panel functionalities to manage users and view trending keywords.

## Features

-   User authentication and registration
-   Keyword search with various filters based upon language, category and date
-   Search results caching
-   User-specific search history
-   Keyword management
-   Superuser control panel
-  Notes Management for students and Assiduous readers

## Visuals
### Login Form


## Installation

1.  Clone the repository:

2.  Change to the project directory:

3.  Create a virtual environment:

5.  Activate the virtual environment:
   
6.  Install the dependencies:

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

## Directory Structure



## Models

-   `Keyword`: Represents a keyword associated with a user.
-   `SearchHistory`: Represents a search history entry for a keyword and it's result search by a user.

## Forms

-   `KeywordForm`: Form for creating and updating keywords.
-   `UserRegistrationForm`: Form for registering a new user.

## Views

-   `home`: Handles news search and displays results.
-   `search_history`: Displays user's search history.
-   `register`: Manages user registration.
-   `keyword_list`: Lists keywords added by the user.
-   `keyword_create`: Handles keyword creation.
-   `keyword_delete`: Handles keyword deletion.
-   `block_user`: Blocks/unblocks a user.
-   `set_limit`: Sets keyword limit for a user.
-   `not_authorized`: Displays not authorized message for non-superusers.
-   `signin`: Handles user sign-in.
-   `control`: Superuser control panel with user management and trending keywords.

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

