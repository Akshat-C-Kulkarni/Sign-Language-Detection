import React from "react";

const ShareButton = () => {
  const shareText = async () => {
    const textArea = document.querySelector("textarea");
    if (navigator.share) {
      try {
        await navigator.share({
          title: "Smart Hands Output",
          text: textArea.value,
        });
      } catch (err) {
        console.error("Share failed", err);
      }
    } else {
      alert("Sharing not supported on this browser.");
    }
  };

  return (
    <button
      onClick={shareText}
      style={{
        padding: "1rem 2rem",
        fontSize: "1rem",
        marginTop: "1rem",
        backgroundColor: "#2ecc71",
        color: "#fff",
        border: "none",
        borderRadius: "10px",
        cursor: "pointer",
      }}
    >
      Share
    </button>
  );
};

export default ShareButton;
