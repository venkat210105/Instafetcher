import fetch from 'node-fetch';

const accessToken = 'IGQWRQM204NlpLdWpnS2tTOFlrdWx3a0I0ZAF9oM3U1X19sTlRTb2VPTmdQaGNZAUTJyeTRKTlpPSE45eENMMVNLR2xUWl9Lcy1uNHVsZAlRmWGtIT0haR0kteW5HLW93MGgxV2hXOFI5LW1NdHF0dGRVOXJpLVNSUzQZD'; // Replace with your actual access token
const mediaId = '18062581690706289'; // Replace with the actual media ID you want to fetch

async function fetchMediaDescription(mediaId) {
    const url = `https://graph.instagram.com/${mediaId}?fields=id,caption&access_token=${accessToken}`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Error fetching media description: ${response.statusText}`);
        }
        
        const data = await response.json();
        console.log('Media Description:', data);
    } catch (error) {
        console.error(error.message);
    }
}

// Call the function to fetch media description
fetchMediaDescription(mediaId);
