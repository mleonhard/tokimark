Tokimarks for Verifying Media Files

- [Intro](#intro)
- [What It's Good For](#what-its-good-for)
  - [Tamper-evident Ballot Boxes](#tamper-evident-ballot-boxes)
  - [Monitoring Voting and Vote Counting](#monitoring-voting-and-vote-counting)
  - [Reducing Lying by Politicians and Media Producers](#reducing-lying-by-politicians-and-media-producers)
  - [Sousveillance](#sousveillance)
  - [Randomization](#randomization)
  - [Data Integrity Checks](#data-integrity-checks)
  - [Digital Signatures](#digital-signatures)
- [How to Use Tokimarks](#how-to-use-tokimarks)
  - [Make a Tokimark](#make-a-tokimark)
  - [Verify a Tokimark](#verify-a-tokimark)
  - [Offline Tokimarks](#offline-tokimarks)
  - [Aftermarks](#aftermarks)
  - [Livemarking a Stream](#livemarking-a-stream)
  - [Watching a Livemarked Stream](#watching-a-livemarked-stream)
  - [Verifying a Livemarked Video](#verifying-a-livemarked-video)
- [Technical Details](#technical-details)
  - [Hashing Algorithm](#hashing-algorithm)
  - [Timestamps](#timestamps)
  - [Tokimark Servers](#tokimark-servers)
  - [Blocks](#blocks)
  - [Afterstamp](#afterstamp)
  - [Implementations](#implementations)
  - [Summary](#summary)
- [Unsolved Problems](#known-problems)
- [Solved Problems](#solved-problems)
  - [Known Upload Leak](#known-upload-leak)
  - [Rate Leak](#rate-leak)
  - [Objectionable Language](#objectionable-language)
- [TODO](#todo)

# Intro
It's 2021 and technology lets us make recordings and share them immediately with people anywhere.
But we can't know if those recordings are original, edited, or labeled with the wrong time.

This document shows a way to know that, called 'tokimarking'.
Tokimarking is a way to show that a particular computer file existed at a particular time
and hasn't been modified since then.

# What It's Good For

## Tamper-evident Ballot Boxes
We can build a ballot box with a light and a camera inside that records continuously.
The camera uses mirrors and lenses to see all around the inside of the box.
The camera gets a video of anybody opening the box, putting anything in, and taking anything out.

The camera software puts tokimarks on the video file.
If someone edits the video, the tokimarks won't validate.
If someone edits the video and puts new tokimarks on the file,
the times of the new tokimarks will be wrong (after the election).

For a public election, we can share the video file with the public.
Then anyone can download the video file,
use software on their own computer to validate the tokimarks,
watch the video, and see if the ballot box was handled properly or not.

## Monitoring Voting and Vote Counting
Tokimarking video cameras can make a verifiable record of election performance.

1. Record citizens voting at polling places.
2. Record inside the ballot boxes.
3. Record election workers opening the boxes and counting the votes.
4. Publish the videos so anyone can download and check them.

Voters can see video of themselves voting, their ballot in the box,
and the election workers taking it out and counting it.
They will have more confidence in the integrity of their election.

We can do this cheaply with phones and simple tokimarking apps.

## Reducing Lying by Politicians and Media Producers
We put people in prison for
[lying to customers about their products](https://www.justice.gov/criminal-vns/case/dennis-balius/update) or
[lying to investors](https://www.justice.gov/usao-ndga/pr/atlanta-ceo-sentenced-prison-securities-fraud).
But we don't do this yet for politicians who lie to the citizens they serve or wish to serve.
And we don't do this for media producers who lie to their viewers.

Some politicians and media producers use disinformation (lies) to influence elections.
They edit videos and images to mislead all of us.
- [Trump retweets doctored video of Pelosi to portray her as having 'lost it' - 2019-05-24 Reuters](https://www.reuters.com/article/us-usa-trump-pelosi/trump-retweets-edited-video-of-pelosi-to-portray-her-as-having-lost-it-idUSKCN1SU2CB)
- [Doctored Political Videos And Social Media - 2019-05-25 NPR](https://www.npr.org/2019/05/25/726941833/doctored-political-videos-and-social-media)
- [Trump tests disinformation policies with new Pelosi video - 2020-02-07 The Verge](https://www.theverge.com/2020/2/7/21128317/nancy-pelosi-donald-trump-disinformation-policy-video-state-of-the-untion)
- [Fox News runs digitally altered images in coverage of Seattle's protests - 2020-06-12 The Seattle Times](https://www.seattletimes.com/seattle-news/politics/fox-news-runs-digitally-altered-images-in-coverage-of-seattles-protests-capitol-hill-autonomous-zone/)
- [Trump shares doctored video of Biden with 'manipulated media' Twitter tag - 2020-09-16 Politico](https://www.politico.com/news/2020/09/16/trump-doctored-video-joe-biden-twitter-415863)
They also lie about the time or location of video and images.
- [Trump posts misleading ad using Ukraine photo - 2020-07-22 BBC](https://www.bbc.com/news/world-us-canada-53500610)

We can use tokimarks to check when a video or image was taken and confirm that it was not altered.
Once this technology is easy to use, many journalists and individuals will use it to boost their credibility.
When someone doesn't use a tokimark, we can ask,
"Why should we believe your video is legit when it has no tokimark?"

## Sousveillance
[Sousveillance](https://en.wikipedia.org/wiki/Sousveillance) means "watching from below".
It means citizens watching what their government workers do.

In a democracy, voters grant permission to government workers to do certain things,
and assign them jobs to perform.
People do sousveillance and hold their government workers accountable
for how they use these permissions and how they perform their jobs.

Tokimarking can be useful for sousveillance.
When someone shares a video or photo of a government worker doing something objectionable,
sometimes the worker says that the video is fake.
If the video has a tokimark, then anyone can verify the time the video was taken
and check if it has been modified since then.
The tokimark helps people to trust that the video is real.

## Randomization
When an app adds a tokimark to a file, it first creates a short scrambled computer code from the file.
This is called a 'hash'.
It sends the hash to a public tokimark server.

Each public tokimark server receives hashes from many apps and from other tokimark servers.
Every second, it combines all the hashes together to make a new hash.

No-one can predict or force a hash.
We can use the hashes as random numbers in lotteries.

A lottery organizer can publish ahead of time that they will use the hashes produced by a particular set of servers
at a particular time as input to a particular very slow algorithm to select the lottery winners.
Afterward, anyone can verify that the lottery organizers followed the process correctly.

Scientists can pre-register the future tokimark hashes they will use in randomisation for experiments.
They can also publish the tokimark of their input data before randomisation.
These practices can reduce
[fraud in medical research](https://blogs.bmj.com/bmj/2021/07/05/time-to-assume-that-health-research-is-fraudulent-until-proved-otherwise/).

## Data Integrity Checks
Sometimes hackers connect to computers and change or destroy data.
Organizations can use tokimarks to know if their computer data has been changed or destroyed.

## Digital Signatures
Digital signatures rely on public key cryptography which is susceptible to advances in technology.
We cannot trust very old signatures because someone could
break an old key and then sign a new document with it.

This is why every public key has an expiration date.
A signature lasts only as long as its public key.

But we can trust a very old signature if it has a tokimark from when the public key was still valid.

Tokimarks let us de-couple signature validity from key validity.
This makes digital signatures more useful.

# How to Use Tokimarks
## Make a Tokimark
You can take a photo or video with an app that supports tokimarking.
After you take the photo or video, the app calculates a short scrambled 'hash' code for the file
and sends the hash to a public tokimark server.
The server sends back the tokimark.
The app adds the tokimark to the end of the file.
This takes about a second.
The tokimark makes the file about N% bigger (TODO: Update with real number).

To make a tokimark for a document, you need software and a connection to the Internet.
The software calculates a hash for your document
and sends the hash to a public tokimark server.
The server sends back a tokimark file.
You can save the tokimark file on your computer.
A tokimark file is a N KB file (TODO: Update with real number).

File storage services will include Tokimark support.
When you upload a document, the app automatically makes a tokimark.
If you already have a tokimark for the document, you can upload the document and tokimark file together.

## Verify a Tokimark
You use software to verify a document's tokimark.
When the software says the tokimark is good, then you can be sure of two things:
1. The document existed at the time the tokimark was made.
2. The document is unchanged.  It has not been altered since the tokimark was made.

When a tokimarked document is on a public website, your web browser verifies it automatically.
You must open the document in a new tab.
The browser bar will show the date, eg "Tokimark 2021-01-06 14:11 EST".

When someone shares a document with you on a file-sharing service,
you can get the document with an app on your phone or computer.
The app gets the tokimark and verifies it automatically.

When someone emails you a document, they can also attach the tokimark file.
Your email software verifies it automatically.

When you have a document and a tokimark file on your computer, make sure you have verifier software,
then select the file and choose "Verify Tokimark".
Your computer must be connected to the Internet for this to work.

## Offline Tokimarks
When you use software to check a tokimark, the software must connect to the Internet to download some data.
You can use software to download this data and add it to the tokimark.
We call this kind of tokimark an "offline tokimark".
Later, you can verify it without connecting to the Internet.

You can't make a tokimark and then make it offline right away.  You must wait until the next day.
This is because tokimark servers prepare the data once a day.

## Aftermarks
You can download a code from the Internet and include it in your video or photo as an 'aftermark'.
Every tokimark server makes a new aftermark once a second.
Nobody can predict what the aftermark will be.

If you find an aftermark in a photo, you can be sure that the photo was taken after the aftermark.
You can use software to check the time of the aftermark.
The software connects to the Internet, to a public tokimark server.

If the photo also has a tokimark,
you can be sure that the photo was taken between the aftermark's time and the tokimark's time.

You can get an app for your phone that displays aftermark QR codes.
Hold the phone up to the camera when you record or stream.
Folks can use software to find out the exact time you recorded your video.

If you're recording audio, you can use an app to play the aftermark as an audio jingle.

Altering a photo or recording to insert an aftermark is very difficult.
The harder it is to alter, the more you can trust the aftermark.
Some things make a photo or video harder to alter.  You can do these things to make your photos & videos harder to alter and therefore more trustworthy:
- Upload the original file created by your camera.  Don't resize or edit it.
- Record high-resolution video and high-quality audio
- Save in raw format or use high quality compression.
  Remember that folks must download the entire file to check the tokimark, so don't make the file too big.
- Include your aftermark in multiple forms: QR code, audio jingle, pole with LED strand, spoken, written on clothing/skin, etc.

When you view a photo or video file, the software can find aftermarks automatically and show you the times.

## Livemarking a Stream
When you stream, you use software to record and send it through the Internet.
The software can add a tokimark to the file once a second.
We call this a 'live tokimark'.
Live tokimarks add about 0.02 Mbps (2.5 KB/s) to the stream bandwidth.

When you stream video, you can hold up a phone with an app that shows a new aftermark QR code every second.
We call this a 'live aftermark'.

When a video has both a live aftermark and a live tokimark, we say it is 'livemarked'.

You can livemark streaming audio, too.  Use an app to play the live aftermark jingle in the background.
Use the same microphone to capture your voice and the jingle.

## Watching a Livemarked Stream

People use software to watch your stream.
The software sees the live aftermark and shows how many seconds the stream is delayed.
People can be sure that the stream really is live.

This works for livemarked streaming audio, too.

## Verifying a Livemarked Video

You can download a livemarked video and watch it later.
You use software to watch it and check the livemarks.  The software can tell you:
1. The video existed at the time the livemarks were made.
2. The video is unchanged and uncut.  It has not been altered since the livemarks were made.
3. The marking interval.

The marking interval is the time between the aftermark and the tokimark for each section of video.
This is the amount of time that a malicious streamer had to edit each section of video before it was tokimarked.
Five seconds is a normal marking interval.
A very short marking interval means the chance of fakery is slim.

# Technical Details
## Hashing Algorithm
Tokimarks use [SHA3-512](https://en.wikipedia.org/wiki/SHA-3).

Every hash is a 64-byte value.

## Timestamps
Tokimark timestamps are the number of seconds since the epoch (1970-01-01T00:00:00Z).

In tokimark format, every timestamp is
a big-endian 64-bit unsigned integer encoded in lower-case hexadecimal.
It always includes leading zeros.

## Tokimark Servers
Tokimark servers listen on TCP port N (TODO: Update with real port number).

Client machines can connect to a tokimark server and perform RPCs to make and verify tokimarks.

Most tokimark servers are public and provide service to any machine on the Internet.

Every tokimark server is independent.

Tokimark servers connect to other servers and call the same RPCs as clients.
There is no special protocol for server-server connections.

## Block Format

A block is a sequence of hashes and a timestamp.
```
$hash0$hash1$hash2...$hashN$timestamp
```

Every hash is a sequence of 64 bytes encoded in lower-case hexadecimal.
Every block must contain 1-447 hashes.

This regular expression matches all valid blocks:
`[0-9a-f]{128}{1,447}[0-9a-f]{16}`.

A tokimark server produces a new block once a second.
It sets the block timestamp to the current time.

The server takes the hash of its previous block and adds it to the new block.
The new block's timestamp must be higher than the previous block's timestamp.

It also gets the latest blocks of other tokimark servers and adds their hashes to the new block.
It adds only hashes of blocks with timestamps that are lower than the new block.
Server blocks form a mesh that is continually extended on one side.

Example block with timestamp 2021-10-22T23:18:50Z:
```
ec67fa2bdc5bb3b3f2010fda6951a8b7e984bf1829f5e0cfa22c31d26d2c57a72b24ae40f6a9d998230ea787528dada13395a26f8b9c7c18c38643a806bcde34d239776717251703c0d2a106c6863cbe1c056d058df630948c1431ec2deee9ca7eada897ed053dad443b9b8b3ad621eaf499891ed823880b230f4a61a971b2b31187b8a4177e6ef0ab85c063e60213f02d4ad9fbb618752fecc2b5c1783aad526c1ea02faf76193af6a12f5b5ab6fda7c8e1bf06a3d4a1ae5bdc86f25724eda8e2dd02f94481e7bea3af151ebb890191437ed3eb78687fa482896701b0e0c630a2f050df8d920a5d02397cdab14cce1d11defe0fcdfd26f2770b90cf7bdd77f900000000617346da
```

## Tokimark Format

A tokimark is a sequence of hashes and a block.

```
e0/tokimark $hash0A$hash0B$hash1B$hash2B...$hashNB $block
```

Every tokimark must contain 2-64 hashes.
Every tokimark is less than 64 KiB in length.

`$hash0A` is the hash of the document's bytes.

`$hash0B` is the nonce.

The hashes form a chain:
- `$hash0A` is the first hash in the chain.
- To calculate `$hash1A`, sort `$hash0A` and `$hash0B`, concatenate them, and calculate the SHA3-512 digest.
  Pseudocode: `$hash1A = sha3_512(concat(sort([$hash0A, $hash0B])))`.
- Calculate `$hash2A` in the same way from `$hash1A` and `$hash1B`.  And so on.
- The final hash (`$hash(N+1)A>`) must appear in `$block`.

This regular expression matches all valid tokimarks:
`e0/tokimark [0-9a-f]{128}{2,64} [0-9a-f]{128}{1,447}[0-9a-f]{16}`.


## New Tokimark RPC
To make a new tokimark for a document,
the client connects to the server's TCP port and sends the request:

```
e0/tokimark-new $document_hash$nonce\n
```

Both `$document_hash` and `$nonce`
are sequences of 64 bytes encoded in lower-case hexadecimal.

`$document_hash` is the SHA3-512 digest of the document's bytes.

`$nonce` is a random 64-byte value.

This regular expression matches all valid New Tokimark RPC requests:
`e0/tokimark-new [0-9a-f]{256}\n`.

Example request for the document "doc0" and a random nonce:
`e0/tokimark-new 5552aa41192b46651fdcb33bdee0d9dd4356307be24ed142089ab615500d1f4e975aae9fd82ee628d466a784722dbf908bab736a761457ad69eb3e19b9a57c6ffe3b5b266eb8038a0c06757399624f1debb3e0df2618341054881010ca14c3782ff13aaf83ce9ca4262b5c435cadfb9f3fd87c63ddbfa89de20d38c1c5f25b94\n`

The server responds with one of:
- ```
   e0/tokimark $tokimark\n
   ```
- ```
   e0/tokimark-transient-error $error_message\n
   ```
- ```
   e0/tokimark-permanent-error $error_message\n
   ```

`$error_message` is any valid UTF-8 string not containing '\n'.
The string length must be 1-200 bytes.

When the server returns a `tokimark-transient-error`, the client may retry the request after a short delay.
If the server returns consecutive transient errors, the client should increase the delay between requests.
We call this 'backoff'.

When the server returns a `tokimark-permanent-error` response, the client must not retry the request.

## TO DO
- Add remaining RPCs
- Add Solved Problems section
- Add Unsolved Problems section
- Update TOC
