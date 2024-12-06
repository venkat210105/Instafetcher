// Import node-fetch as an ES module
import fetch from 'node-fetch';

// Define the access token and API URL
const accessToken = "IGQWRQM204NlpLdWpnS2tTOFlrdWx3a0I0ZAF9oM3U1X19sTlRTb2VPTmdQaGNZAUTJyeTRKTlpPSE45eENMMVNLR2xUWl9Lcy1uNHVsZAlRmWGtIT0haR0kteW5HLW93MGgxV2hXOFI5LW1NdHF0dGRVOXJpLVNSUzQZD";
const url = `https://graph.instagram.com/me/media?fields=id,caption&access_token=${accessToken}`;

// Fetch media IDs and captions
fetch(url)
  .then(response => response.json())
  .then(data => {
    console.log("Media IDs and captions:", data);
  })
  .catch(error => {
    console.error("Failed to fetch media IDs:", error);
  });
