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
![Search results for Ronaldo and Arab language](https://lh3.googleusercontent.com/pw/AP1GczOl4mdtYrGLfuc1MZbuxwjpGMPUPyiPHk6-FNw8uC0WYQQ-BMdWjlrSgsDACqkXt0JwN1dh65AnzJiJFgKkZtZoj8x37EA_9i8byOCPfk60Wfh5CvEfxeFii7TrqIayQMoXvzYFP5gFrIp-QYVMi8XsgJ_OUxVmEHLraTslLUulA_80LLvbwO_VejZq6Bd4JGxmWVlaxhe38loWWfxjS3WHowtcjF3E0M7IV6CPMZ5rtHqTKpKZ8kFF589f1Zwuu2p9AU9ZoLJwmKA6mUA2qqtjo14IR4HK7Yylmi0I1AwlNu5n2uO2n-bFE56DY4O_2DlfvcZt3ce5q_0G1sWhAgmGSSFVJj6lM58tbOODNv0mtS3l01ag5ugv8JdZ7aoC2eQfenzTpbsNRhyufXnZwTCEq-1u85-8nM0eTSid_eNboGEn2SE4FqQMxpZY9ZGN0goEfp4zViJBr5E8VSBr_q8TIZ8pkqh5nbgffOi1FOn263bK_IVJrlO5wlce9wUbNnt5tLy3xdbRKC_4NWd7q_6YXB4yhmd5FXXwia5dmjayH2NJPap3mmMpwj18_vO-bNBaOi8pHwEbMdsilMOWWVfLFThW4zDgMIs_IWvFVXJ5krpGApb8pP1dficpmUa1AAlqgaxSBCtlqtUoW6pcpHLfd5RT9PCBqRQRvnQSaSGr1yDFDEC8UPHxXhdzr4Ww3eyuwTWQsKBbiFeX_IJqD5LdoregZHMD6wZAF2LQQucMEc8dGR97xgTQR2e998Xume6T2wyL3AhE1EQTGSdF5qE0Rx52X2-t8R6CK1XO4VFAeK0m0QByHtA18pFbDa6tSknbBirK10y1G_st3lSws19C_AWACU4y9zZyOCAmCdtNTQgwETtyfRkRo7cHNUQE3rcIUbx2JZPFpOnfw2MCwDkQ1g=w1649-h928-s-no-gm?authuser=0)

### Registration Form

![enter image description here](https://lh3.googleusercontent.com/pw/AP1GczN-ikWpm3YvX4pEsvUrbqlBvBowfVDTetA0CWhF9I1Wj83KcwqHmIy_jhh1hz59x6j2T2gtXqlBNxsDpDpDmPevK3Eh5UpKLTuGScx_Hmj6QtvRcLr0RX51njG4b9HDejAgJ3_d4tR-4LgrY-TdgW2EGcp-8MDkLg32-h5rJjz0b8zKIdP41wzOvoZaeB0DN6DohEMiPzgxFjfXKLkhcwzSY-s6JnFIhmdtSlRF8iffqeMKTiQNayusMWC8SYskoPZGn3CiZ75jGIGFFbUmcQG7wSHGLE6eWMr186gGq_N7N5pp-VDxLUys-SDtb6mIxsqYLdemVwPQS3Kvow-FJwX0LSCpUBPVcVnG86hIA5VdH2Rx9yv_q9x_TrSXj9lULvn4rvM25iF3pJw48xQlqEPd0R_rPkgfNKW2J3YEpCcYjUuZyCnsFnrbnaezX6I5DeAPyrGUFOcx3_TXwvBPw1R3uREXWi0K-yaL-pyzGCBDXUajDFNWCcf0fr32Wb24PxbQhxD0QuDgK7JWb8x8IjKCv1IZGUIMHjLMfvV2SIkkOqT26lWRH1rNLaq0Q3iecIp0E2Wt8sqxQ7HY80uykginm1bYKqZ2oLGZwtE-S1vNGvIOpkvrNReqLQe97E_GYxAXe_qOEiRobbcloItdIRDlr9XzNL9a9soXNytiAOyEfybfwyhoDnFLn1amO5eHOaeZDXN67B7KskGlDOZKcFY2ByDJ6_l0lg47vrM6ooU-oNoEmXL1axQnCe3zHQuDU0K0FQr_lignP7YeOfbTRdIAzkoL8FLZb_-m93gLGb0mWm-Dr6DehXGGs72ppggb_AfYYXVulqjWz_x1rwtdM-2pqf6QfOwfQdM9vnXb0VyyxvGJ6LK8u7il9ztsmPQRL6QaZiLkrdihKNlVwTyboWUchA=w1649-h928-s-no-gm?authuser=0)

### Login Form

![enter image description here](https://lh3.googleusercontent.com/pw/AP1GczNTjYM54Hs1hcIVwvjuL1UU85XLqrdo438RU6_ZUrVTgmXsDDf7kybGx_4Y6oBhiv51_wtVTlotKwBKAiYLunS7jPKFTfkF10Yijv5tCsAWG0ijkLvli1e63rTsHH7FqdET_3TOL_mhNYp463jZ7aV96hwWB7CBiqlWGQzkUpBaL_NMsrV3BtOGTcNBFK5B6j6ICTeiWBe1BUqe9JFO05sRcud5xkRYSyVPFbQGbJwzyT2v6i03g_ghB47TymV2ax5D7r6_-bAC9cALV-8l-_N-BB3m11uD7qTEnI7YmCrahcAvRpuUYPDJtD0RIt7c5A5cnvK0i1tmuSIU5WRmib20PA-3-tVCxCL5WarvdOIcGnNc_Ok85J0xVswyBqQ5iXELEh-JM5frog4KZvWXvmfBfcx60ThzJwgB0S8pvN1Pqa_DLNePnJhr9HwQ8nW6_10rUOghN_IwFbyVXFjYNu8K02xYvs60lpP5vjCMck1A5WFu4kUKXLt_Iz002h_PWHIohufQ6kpeIVD3LoVYuXKrgH7spRH_Vo6pY-dYNB_Ic9LOBx6XQPuWWPycS-qhviZh-GOWE3TEUkc9sYQ8iztgcWu30hqwycSbnbO7qc-e15ErXanIaVEshYb4mM-UUmDk18WIsr72ugi4v9Ig1YWjJc2n5JBp_jO4pi12IEa87ST5HZ8CUVtSe3_v3nAveM_-3V-AWNhUOdOmb44tsPhetSrKdN5z5A2A3bAIX2X6vNdy6dNhRwh3bAQTa6byYkj8Cd1GZioQfHx7DEdazvRX70c0DSzeVCIRNsqgtlGAht4PxBukqIagrqdkbE4lQGIdUM-gVJWoBJ3K1s6wGJXLMtdxoJuRJudCEjOzvKEmdFmgpu_xg0Z88FECzMDxO3PV5Udi7VmUrvljxREUxYKbrg=w1649-h928-s-no-gm?authuser=0)

### Admin Panel

![enter image description here](https://lh3.googleusercontent.com/pw/AP1GczPax9rz0AUJDeWG_lAW6yiM2fMqcQH96SnZDgvff3ECOXzPefO6mkCWncbkLJKXZoNIW-Qg5jh7qwsG999tIlEkKqajhJyqdwPhYS3kwIuvgoQ6ehk1dcy_c4wJNhktFhPZRsagr2NEB5iLJRYRcmfrle14V-af_QjBx694vywJ7OD1MLX-dYtbwboCP6Zz9oK6BdzlOAW5cPq4WZbkDbIb1YUl2BnDZ5fGjlUrsAUjx3eYEdWWGjS5H6fwkX_785h27fd3j5o04V83-v2aDbtfRimmeJVsJheTG-0S2Hxq7tcYSlAj5piTAMWyMrg1-ZxDGth_x1vfes0ujgh_-K8I7eZd_JMJlb_2vDMf2nNO6auPExn6us-1BFy0Bp9kp7QLONMJYYV5OLy4Yymm5W1jmfaTDshMDw1q8cG38d_JAu39S9Nz2GTKU6Fln6BKzZB31psg_XY49JVi-ML9_e-K2IBsoC_hj_eE6kphL8qCMqjFvMZML3HArUpVbmT7fPPQ7bEn6_-GTJ608e_m33cONVNC834mauC93Fk7nC2upPuy_ttWveyGFVhI-RiQ4KKM-gR4CdOS-J6FG4X3PGBbDB7DEH05TfUZ9LjQ3JPELLeQEktyINLUxvJyel-o_ldKYMLC64aXs64AOprNBw4wFRoz6VmhSwrY7uUSpKkwh1BW4hYY4M31WkKVl7hB7Xnt3MtX4PAyZKeJIlb0UXF-xHoGeHSa9h4vzLbHoAru6mSugBBNqoi0hmP9ifvtmJBwW9IPLrKsG_2XMla85FA36sLiZihk8DgjNDE6arFAVDjoZ3mJgRKDWlNWkfp3qwtD8AsZjl1AcvpXY5XkfeY7POtqzTcT95HyBJYYrMt9vb1lPQc9ojYcZtf59T5WjRp7Eeow2l77aJmm9TXQeH1reg=w1920-h819-s-no-gm?authuser=0)

### Trending Keyword

![enter image description here](https://lh3.googleusercontent.com/pw/AP1GczPCQgpY0VGLRKr16lrX2dDkcWCu5ihGZ_Qvcrup_JYlPSsr3mBBsLH8ZEg6m8cNvs5v3XckLLGQbtuX_t1JgNc8AEeOE6tB5JqDffxpVlB_XAXaFmeT_TR1vds6eBcfcew5b5EMKUJbZzZYhJ3HcZk9p1vrZHIAc8Cq3NLT9Z9I7R0i6vXkvg4XiFRqgywu0KP5Df_XQTRfQZDMwH0xf75YceILf1rpUqWD4rDW260PNti3RB2nuBkqbQTZ7SLNkjvpYkea8k-_6TeSSsNVoneuT3a8qEI3kamsNuVdo7La5-v1vXArbmwv3r7q_4iNSpmpg5TUk-hKT0Hix1_-DKqV3bJRGoaVGgB5ChCPX-2dAkrlUjcNlR35p4RoWKT21_uGXfiJDYtp3PhTPsz6rPWZ2tk1PUJOMAEFgJGDMUYtZZaAk8j5p1h9RV5glcylTy1qvtZe8Yjl_VXJGikoxNrvSOxCe5aD5y3RPJB4H-T_7X3dt2j17HGMST6MT41Zk7S29aX1PTD0VhucsRXYj7PVgfvWr_3cXzsJcK_LkFrkwddZw9nzBHEJ0WeWykVoc0jwaf5wbSBuiFROvQTMh9S5hZDeu6c7i4BGLa__akb4NbjNMqPBx4Zso6rtfgk-EzEeJXdvjJpx1NjUM1v77c6kdXYB1C4ZQ3CkiHn2qIORbHaH7-klf93NWw5rlbxJpDflL6j1F9T8X1uxmc-bZIcUX0CvpkA_uBhMwlXXsWb-QFtlisf71SpSgzHJihW6V2AfQdpKJCnfxxJyTibbMc1qfryd5Y20bH67fRt0O2wExQuPM5D4VI4GNrODyGh9hnTDqC9-guY5CASqawYL4Gv6ctOS5LGZGA-_rd4ZO8rRdtQbmXy8x9dCZiVZ_ODDdeVZ0AwpJVI4Gjs1Fy-EvxxfFA=w1920-h757-s-no-gm?authuser=0)

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
