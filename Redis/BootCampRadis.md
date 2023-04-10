# Redis
link [Redis](https://redis.io/)

<details>
<summary>About</summary>
<p>  Redis is an open source (BSD licensed), in-memory data structure store used as a database, cache, message broker, and streaming engine. Redis provides data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, geospatial indexes, and streams. Redis has built-in replication, Lua scripting, LRU eviction, transactions, and different levels of on-disk persistence, and provides high availability via Redis Sentinel and automatic partitioning with Redis Cluster.
</p>
</details>

<details>
<summary>Troubleshooting with install</summary>
If after connecting to a VPN on Windows, bash loses network connectivity, try this workaround from within bash. This workaround will allow you to manually override the DNS resolution through /etc/resolv.conf.

Take a note of the DNS server of the VPN from doing ipconfig.exe /all
Make a copy of the existing resolv.conf sudo cp /etc/resolv.conf /etc/resolv.conf.new
Unlink the current resolv.conf sudo unlink /etc/resolv.conf
sudo mv /etc/resolv.conf.new /etc/resolv.conf
Edit /etc/wsl.conf and add this content to the file. (More info on this set up can be found in Advanced settings configuration)

Copy
<code>[network]
generateResolvConf=false</code>
Open <code>/etc/resolv.conf</code> and </br>
a. Delete the first line from the file which has a comment describing automatic generation</br>
b. Add the DNS entry from (1) above as the very first entry in the list of DNS servers.</br>
c. Close the file.</br>
Once you have disconnected the VPN, you will have to revert the changes to /etc/resolv.conf. To do this, do:

cd /etc
sudo mv resolv.conf resolv.conf.new
sudo ln -s ../run/resolvconf/resolv.conf resolv.conf
<p> <a href="https://learn.microsoft.com/en-us/windows/wsl/troubleshooting#wsl-has-no-network-connectivity-once-connected-to-a-vpn" title="Troubleshooting via VPN"> Troubleshooting via VPN </a></p>
</details>