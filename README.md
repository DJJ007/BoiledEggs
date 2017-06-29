# BoiledEggs

This is the source code repository for a simple web application created in django. 

# What is this web app?

This app simply demonstrate the use of MVC Pattern of django. Nothing more. I created a Models, and a view which extract info from model and render it in html.



## Fork the repository

First fork the [NischalLalShrestha/BoiledEggs](https://github.com/NischallalShrestha/BoiledEggs) repository to your personal Github account:

![Fork button](contributing/images/fork.png)


## Simple changes

For simple changes like typo corrections you can use the Github online editor:

* Open your local fork page on Github,
* go to *README.md* file in any chapter,
* press the *Edit* icon (pen)

and you can edit the chapter directly on github.com.

![Edit button](contributing/images/edit.png)

Markdown syntax is used to edit the individual pages of the tutorial.

![Github editor](contributing/images/github_editor.png)

Save your changes and create a pull request as explained below.

## New content and complex changes

For adding new chapters, writing longer snippets of text or adding images, you need to get a copy of the tutorial to your local computer.

Either use the Github app for your operating system (mentioned above) or `git` command line to get the repository locally. You get the repository address from the front page of your own Github repository fork:

    git clone git@github.com:yourgithubusername/tutorial.git

Then, create a branch for your new changes to sit in. It helps to call the branch something related to the changes you are going to make.

    git checkout -b contributing

    $ git status
    On branch contributing
    Untracked files:
      (use "git add <file>..." to include in what will be committed)

        contributing_and_editing_this_book/images/gitbook.png

    $ git add contributing_and_editing_this_book/images/gitbook.png

    $ git commit -m "Added gitbook editor screenshot"
    [contributing fe36152] Added gitbook screenshot
     1 file changed, 0 insertions(+), 0 deletions(-)
     create mode 100644 contributing_and_editing_this_book/images/gitbook.png

    $ git push
    Counting objects: 11, done.
    Delta compression using up to 8 threads.
    Compressing objects: 100% (5/5), done.
    Writing objects: 100% (5/5), 266.37 KiB | 0 bytes/s, done.
    Total 5 (delta 1), reused 0 (delta 0)
    To git@github.com:miohtama/tutorial.git
       b37ca59..fe36152  contributing -> contributing.

