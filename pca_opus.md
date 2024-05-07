# Spectral Reduction Allegory - Matrix factorization of movies and users

labels: PCA, publication

https://www.reddit.com/r/MLQuestions/comments/1cloi3k/how_do_i_get_team_features_based_on_player/l2wq7o6/?context=3

Consider a dataset where N people each watched the same M films. For each film, the people got to pick any number of tags to associate with the film, choosing from a collection of K tags. (Let me know if setting up the notation like this is helpful or confusing). Let's assume all K tags got used at least once. Pretend N and M are reasonably large, say on the order of millions of people and movies, and let's say K is on the order of hundreds of thousands of tags.

So now we've got this dataset of users, movies, and tags. The tags bridge the gap between users and movies. If we collect and rank all the tags associated with some movie, we'd have a pretty good fingerprint for the themes and genre of the film.

Similarly, if you picked a person at random, you could collect and sort all the tags they'd ever used, and treat the resulting histogram as a characterization of the kinds of movies that person likes to watch.

What do we get if we just collect and rank all of the tags? We get a ranking of genres and themes sorted in order of "importance" to the users and movies in the dataset.

Do we really need all of those tags though? Now that we have that importance ranking, it looks like there are a couple of tags that people just sorta pulled outta their asses. The people who came up with these tags generally used other more normal tags, but every now and then someone just wrote something weird down, and so we have a lot of tags that only apply to handful of users/movies or maybe even just one.

Is it even a "genre" if there's only one film in it? Fuck it, let's ignore those tags. Let's say we drop some of the more niche genres too. You know what? I bet we can approximate those "genre fingerprints" we developed earlier with just the top handful of most important genres. How many sections did there used to be in a video store... like 4-5 right? maybe 10-20 if it was a fancy video store? This will come at the cost of those "fingerprints" we constructed earlier being unique, so we won't be able to tell some number of similar people/movies apart from just their tag profiles, but we'll have the information we'll need to decide if we want to watch a movie ourselves or recommend it to a friend.

We started with K tags, a feature space with dimension K. We ordered the tags and kept only the most dominant K'. The new dimension K' space is more compact and pushes items that are similar close together.

Something that's nice about our dataset is that we could just collect this in a spreadsheet if we wanted. Put the people along the rows and the movies along the columns, and put the tags a user ascribed to a movie in the corresponding cell. In fancy math speak, this kind of 2D grid is called a matrix. The number of unique tags (K) is a property that is called the "rank" of the matrix. When we flushed out the low importance tags, the updated matrix has rank K'. By reducing the rank of the matrix in this way, we effectively perform a kind of clustering operation on users and items simultaneously that condenses our feature space into just the most important features.
