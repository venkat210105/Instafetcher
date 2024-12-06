const fetch = require('node-fetch');

// Replace these placeholders with your actual values
const accessToken = 'YOUR_ACCESS_TOKEN';
const mediaId = 'YOUR_MEDIA_ID';

async function fetchInstagramComments() {
  try {
    const url = `https://graph.instagram.com/${mediaId}/comments?access_token=${IGQWRQM204NlpLdWpnS2tTOFlrdWx3a0I0ZAF9oM3U1X19sTlRTb2VPTmdQaGNZAUTJyeTRKTlpPSE45eENMMVNLR2xUWl9Lcy1uNHVsZAlRmWGtIT0haR0kteW5HLW93MGgxV2hXOFI5LW1NdHF0dGRVOXJpLVNSUzQZD}`;
    const response = await fetch(url);
    
    // Check if response is okay
    if (!response.ok) throw new Error(`Error: ${response.statusText}`);
    
    const data = await response.json();
    console.log("Comments Data:", data);
  } catch (error) {
    console.error("Failed to fetch comments:", error.message);
  }
}

fetchInstagramComments();
