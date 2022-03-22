# Challenge

## Intro

This document containts the information about what you need to do. Please do it following the best understanding you get from what is described here.

## Documentation

Check TMDB documentation for more information how to use the api https://developers.themoviedb.org/3/getting-started/introduction

## Tasks

The following tasks should be done in the service. It is our chance to know how you work and
your chance to learn a gist about what we expect. Consider each bullet point as a separate task.
Do as many as you can manage.

- Broken images

    - Description: Users are reporting that the images from movie posters are broken, they are expecting an absolute path to an image URL that is 500 pixel wide.
    - Expected: movie poster images are 500 pixels wide and contain the full url address.

- Genre names

    - Description: Users are reporting the response `genre_ids` from search is only a list of numbers. 
    - Expected: there should be genre name in the response.

- Sorting parameters

    - Description: Add sorting parameter to movie search so the response can be sorted by title, release_date or vote_average:
        - add by a single field
        - add by multiple fields
        - allow reverse order
        - support pagination

- Movie rating endpoint

    - Description: Users would like to have a movie rating endpoint. The MVP should accept authentication as a guest on TMDB and add a new endpoint for rating a movie.

