# bigbang
BigBang is an opinionated boilerplate for and by ankur gupta used for development of software applications.

**Software Stack**
- Deployment
  - Docker

- Operating System
  - Ubuntu ( Minimal Ubuntu 18.04 LTS )
    - Python 3.7
    - golang
    - ssh port changed

- Databases
  - Redis
  - MySQL
  - Elasticsearch
  - Druid

- Caching and Message Queue
  - Redis (Streams for queues)

- Load balancer and Webserver
  - nginx

- Logging
  - ELK based setup for logging

- Web Framework
  - Django
    - django-allauth - Improved user registration including social auth
    - django-compressor - Compress JavaScript/CSS into a single cached file
    - django-debug-toolbar - Configurable panels to debug requests/responses
    - django-environ - Environment variables
    - django-hijack - Admins can log in and work on behalf of other users without having to know their credentials
    - django-import-export - Import/export data more easily with admin integration
    - django-organizations - Multi-user accounts for Django projects
    - django-silk - Live profiling and inspection of HTTP requests and database queries
    - django-sql-explorer - Share data via SQL queries
    - easy-thumbnails - Image thumbnails for Django
    - django-devserver - A drop in replacement for Django's built-in runserver command.
    - django-ses - A Django email backend for Amazon's Simple Email Service.
    - django-searchable-select - A better and faster multiple choice widget with suggestions.
    - django-uuidfield - A UUIDField for Django.
    - django-versatileimagefield - A drop-in replacement for django's ImageField that provides a flexible, intuitive and easily-extensible interface for quickly creating new images from the one assigned to the field.
    - django-merchant - A Django app that provides helpers for multiple pluggable payment backends.
    - django-meta - a pluggable app to allow Django developers to quickly add meta tags and OpenGraph, Twitter, and Google Plus properties to their HTML responses.
    - django-robots - A Django app for managing robots.txt files following the robots exclusion protocol.
    - django-seo2 - Provides a set of tools for managing Search Engine Optimisation (SEO) metadata for Django sites.
    - django-sql-explorer - Easily share data via SQL queries, right from Django
    - blog engine
  - Test App that connects to 
    - payment gateway
    - all databases
    - logging server
    - setup(s) debugging tools

