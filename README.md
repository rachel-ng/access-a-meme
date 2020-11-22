# access a meme 

demo @ https://youtu.be/gAMH2hTDOB8

<img src="https://github.com/rachel-ng/access-a-meme/blob/main/static/img/bonus_meme.jpg" alt="meme with 'access-a-meme' shoving 'this text' with weird characters"></img>

## Inspiration

we love memes! but those "Official sources stated that is false and misleading" tweets? inaccessible. 

fonted display names, bios, and tweets? inaccessible. 

let's make it so that people who use screenreaders can enjoy these things with us, rather than be bombarded with a math equation or silence. 

images too! alt text isn't used often enough (and we don't really cover it in the video,,) and we need more of it

## What it does

remap text with special / fonted characters
add a (bad) description of what's going on images! 

## How we built it

- tweepy and the twitter API, for all the twitter things 
- python, for just about everything 
- flask, for the web app 
- ibm vision api, for image descriptions 
- a dream 

characters originally "borrowed" from https://lingojam.com/FancyTextGenerator
we remapped them to their corresponding alphanumeric characters and tossed it into a csv 

the web app spits out a user timeline (specifically @racheloniine's) and "translates" all fancy text to normal text

## Challenges we ran into

we originally didn't want to use the twitter API to be honest. we really just wanted to improve the "feature" as a whole! but we had to so we make our own little timeline viewer 

we also originally intended to use a different API (the google one specifically) and wanted to incorporate tweet interactions into the descriptions / created alt text of images, but that ended up being more of a stretch goal 

## Accomplishments that we're proud of

actually getting the mapping to work! we're so happy it worked! 

## What we learned

do not join hackathons with 2 people and a lot of ideas. it doesn't work out too well :') 

## What's next for access a meme

better interpretations in general! 

making "ⓘ  𝗢𝗳𝗳𝗶𝗰𝗶𝗮𝗹 𝘀𝗼𝘂𝗿𝗰𝗲𝘀 𝘀𝘁𝗮𝘁𝗲𝗱 𝘁𝗵𝗮𝘁 𝗶𝘀 𝗳𝗮𝗹𝘀𝗲 𝗮𝗻𝗱 𝗺𝗶𝘀𝗹𝗲𝗮𝗱𝗶𝗻𝗴"

read as "Warning Official sources stated that is false and misleading" would've been super cool! 

and better image analysis, we were originally thinking of incorporating data from quote retweets and replies but we wanted to focus on core functionality first!  



# we're doing this so very last minute and apologize for our errors! 
