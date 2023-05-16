<<<<<<< HEAD
# Postmortem

Upon the release of Alx School's System Python  project, approximately 12hours (EAT), an outage occurred on an isolated Ubuntu 20.04 container running on Apache server. GET requests on the server led to `500 Internal Server Error`'s, when the expected response was an HTML file defining a simple Holberton site..

## Debugging Process

Bug debugger Brennan (BDB... as in my actual initials... made that up on the spot, pretty
good, huh?) encountered the issue upon opening the project and being, well, instructed to
address it, roughly 19:20 PST. He promptly proceeded to undergo solving the problem.

1. Checked running processes using `ps aux`. Two `apache2` processes - `root` and `www-data` -
were properly running.

2. Looked in the `sites-available` folder of the `/etc/apache2/` directory. Determined that
the web server was serving content located in `/var/www/html/`.

3. In one terminal, ran `strace` on the PID of the `root` Apache process. In another, curled
the server. Expected great things... only to be disappointed. `strace` gave no useful
information.

4. Repeated step 3, except on the PID of the `www-data` process. Kept expectations lower this
time... but was rewarded! `strace` revelead an `-1 ENOENT (No such file or directory)` error
occurring upon an attempt to access the file `/var/www/html/wp-includes/class-wp-locale.phpp`.

5. Looked through files in the `/var/www/html/` directory one-by-one, using Vim pattern
matching to try and locate the erroneous `.phpp` file extension. Located it in the
`wp-settings.php` file. (Line 137, `require_once( ABSPATH . WPINC . '/class-wp-locale.php' );`).

6. Removed the trailing `p` from the line.

7. Tested another `curl` on the server. 200 A-ok!

8. Wrote a Puppet manifest to automate fixing of the error.

## Summation

In short, a typo. Gotta love'em. In full, the WordPress app was encountering a critical
error in `wp-settings.php` when tyring to load the file `class-wp-locale.phpp`. The correct
file name, located in the `wp-content` directory of the application folder, was
`class-wp-locale.php`.

Patch involved a simple fix on the typo, removing the trailing `p`.

That was all needed!
=======
# Server requests failure report
Last week, it was reported that the platform was returning 500 Error on all requests made on the platform routes, all the services were down.  90% of the users were affected. The root cause was the failure of our master server web-01.

## Timeline
The error was realized on Saturday 27th August 1000 hours (West Africa Time) when Mr Williams saw the master server lagging in speed. Our engineers on call disconnected the master server web-01 for further system analysis and channelled all requests to client server web-02. They soled problem by Sunday 27th August 2200 hours (West Africa Time).

## cause and resolution
The platform is served by 2 ubuntu cloud servers. The master server web-01 was connected to serve all requests, and it stopped functioning due to memory outage as a results of so many requests because during a previous test, the client server web-02 was disconnected temporarily for testing and was not connected to the load balancer afterwards. 


The issue was fixed when the master server was temporarily disconnected for memory clean-up then connected back to the loadbalancer and round-robin algorithm was configured so that both the master and client servers can handle equal amount of requests.

## Prevention against such problem in future
- Choose the best loadbalancing algorithm for your programs
- Always keep an eye on your servers to ensure they are running properly
- Have extra back-up servers to prevent your program fro completely going offline during an issue
>>>>>>> 21c35ece6033d103b3c189a01f16aaaae15e1f54
