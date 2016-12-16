import webbrowser
import os
import re

# Styles and scripting for the page including responsivne and mobile
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background-color: #66B9BF;
        }

        .container2 {
          display: flex;
          flex-wrap: wrap;
        }

        .col-md-6 {
            background-color: #66B9BF ;
        }
        h2 {
            color: black;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #07889B;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
            
        @media screen and (min-width: 1000px){
            .col-md-6 {
                width: 25%;
            }
            h2 {
                font-weight: bold;
                font-size: 16px;
            }
        }

        @media screen and (max-width: 1000px){
            .col-md-6 {
                width: 33.33%;
            }
            h2 {
                font-weight: bold;
                font-size: 16px;
            }
            img {
                height: calc((80% - 10px)/1.5);
            }
            .hanging-close {
                width: 60px;
                height: 60px;
                right: -45px;
            }
        }

        @media screen and (max-width: 750px){
            .col-md-6 {
                width: 50%;
            }
            h2 {
                font-weight: bold;
                font-size: 13px;
            }
            img {
                height: calc((100% - 0px)/2);
            }
            .modal-content {
                width: 60%;
                margin-left: 10%
            }

            .hanging-close {
                width: 45px;
                height: 45px;
                right: -30px;
            }
            }
        

        @media screen and (max-width: 500px){
            .col-md-6 {
                width: 100%;
            }
            h2 {
                font-weight: bold;
                font-size: 13px;
            }
            img {
                height: calc((100% - 0px)/2);
            }
            .modal-content {
                width: 50%;
                margin-left: 10%;
            }
            .hanging-close {
                width: 40px;
                height: 40px;
                right: -30px;
            }
        }

        @media only screen and (max-device-width: 800px){
           body {
            background-color: #07889B;
           }
           .col-md-6 {
                width: 50%;
                background-color: #66B9BF;
            }
            h2 {
                font-weight: bold;
                font-size: 180%;
                color: black;
            }
            img {
                height: calc((100% - 0px)/4);
            }
            .modal-content {
                width: 100%;
                margin-top: 80%;
            }

            .hanging-close {
                width: 35%;
                height: 35%;
                right: -200px;
            } 
        }

        @media only screen and (max-device-width: 480px){
            .col-md-6 {
                width: 100%;
            }
            h2 {
                font-weight: bold;
                font-size: 240%;
                color: black;
            }
            img {
                height: calc((100% - 0px)/4.5);
            }
            .modal-content {
                width: 100%;
                margin-top: 80%;
            }
            .hanging-close {
                width: 40%;
                height: 40%;
                right: -240px;
            }
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
    <div class="container2">
      {movie_tiles}
    </div>  
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
