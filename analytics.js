
const baseURL = "http://localhost:8000"; // Removed /analytics to prevent double path


async function loadAnalytics() {
  try {
    //  Fixed double path: it was baseURL + "/analytics" but baseURL already includes it
    const res = await fetch(`${baseURL}/analytics`);
    const data = await res.json();

    //  Update stats on page
    document.getElementById("itemCount").textContent = data.stats.item_count;
    document.getElementById("userCount").textContent = data.stats.user_count;
    document.getElementById("avgItemName").textContent = data.stats.avg_item_name_length.toFixed(2);
    document.getElementById("avgUserName").textContent = data.stats.avg_user_username_length.toFixed(2);
    document.getElementById("maxItemName").textContent = data.stats.max_item_name_length;
    document.getElementById("maxUserName").textContent = data.stats.max_user_username_length;

    // Incorrect: data.plot does not exist
    // Correct: backend sends image as base64 in data.plot_base64
    document.getElementById("plot").src = `data:image/png;base64,${data.plot_base64}`;
  } catch (err) {
   
    console.error("Error loading analytics data:", err);
  }
}

// 
loadAnalytics();
