import axios from "axios";
import React, { useEffect, useState } from "react";
import Swal from "sweetalert2";
import useUserStore from "../../store/userStore";
import { GetPlaceDetails } from "../../service/GlobalApi";

const Analytics = () => {
  const { user, fetchReview, setOverallAnalysisMain } = useUserStore();
  const [overallAnalysis, setOverallAnalysis] = useState(null);

  const handleFormSubmit = async (e) => {
    e.preventDefault();

    const fd = new FormData(e.target);
    const data = Object.fromEntries(fd.entries());

    const postData = {
      textQuery: data.search,
    };

    const result = await GetPlaceDetails().then((response) => {
      console.log(response.data);
    });

    if (user.reviews.length === 0) {
      Swal.fire({
        title: "Loading...",
        text: "Fetching data from Google API",
        allowOutsideClick: false,
        didOpen: () => {
          Swal.showLoading();
        },
      });

      Swal.fire({
        icon: "success",
        title: "Data Fetched Successfully",
        text: "Google API data has been retrieved.",
      });

      console.log(googleData.data);
    } else {
      console.log(user.reviews);
    }
  };

  const handleReviewAnalysis = async (e) => {
    e.preventDefault();

    const fd = new FormData(e.target);
    const data = Object.fromEntries(fd.entries());

    Swal.fire({
      title: "Analyzing...",
      text: "Processing your review",
      allowOutsideClick: false,
      didOpen: () => {
        Swal.showLoading();
      },
    });

    try {
      const response = await axios.get(`http://127.0.0.1:8000/ai/predict`, {
        params: {
          input: data.review,
        },
      });
      const responseData = response.data;

      const formattedData = {
        content: data.review,
        created_at: new Date().toISOString(),
        analysis: {
          sentiment: responseData.Sentiment,
          emotion: responseData.Emotion,
          keyThemes: responseData["Key Themes"],
          painPoints: responseData["Pain Points"],
          urgency: responseData["Urgency Level"],
          recommendation: responseData.Recommendations,
        },
      };

      try {
        await axios.post(
          `http://127.0.0.1:8000/user/${user.email}/review`,
          formattedData
        );

        Swal.fire({
          icon: "success",
          title: "Analysis Complete",
          text: "Your review has been successfully analyzed and saved.",
        });

        fetchReview();
      } catch (error) {
        Swal.fire({
          icon: "error",
          title: "Error Saving Data",
          text: "Failed to save the analyzed data.",
        });
      }
    } catch (error) {
      Swal.fire({
        icon: "error",
        title: "Error",
        text: "Failed to analyze the review.",
      });
    }
  };

  const findOverallAnalysis = async () => {
    const reviews = user.reviews;

    if (!reviews || reviews.length === 0) {
      console.error("No reviews found to analyze.");
      return;
    }

    let analysisString = reviews
      .map(
        (review) =>
          `review: ${review.content} created at: ${new Date(
            review.created_at
          ).toLocaleString("en-US", {
            year: "numeric",
            month: "long",
            day: "numeric",
            hour: "2-digit",
            minute: "2-digit",
            second: "2-digit",
          })}`
      )
      .join(" ");

    if (!analysisString) {
      console.error("Analysis string is empty.");
      return;
    }

    Swal.fire({
      title: "Analyzing overall reviews...",
      text: "Processing the overall analysis based on reviews.",
      allowOutsideClick: false,
      didOpen: () => {
        Swal.showLoading();
      },
    });

    try {
      const response = await axios.get(
        "http://127.0.0.1:8000/ai/predictOverall",
        {
          params: { input: analysisString }, // Ensure this is a valid string
        }
      );
      const data = await response.data;

      setOverallAnalysisMain(data);

      Swal.fire({
        icon: "success",
        title: "Overall Analysis Complete",
        text: "The overall analysis has been successfully fetched.",
      });
    } catch (error) {
      console.error("Error during overall analysis:", error);
      Swal.fire({
        icon: "error",
        title: "Error",
        text: "Failed to fetch the overall analysis. Please try again later.",
      });
    }
  };

  // useEffect(() => {
  //   const fetchUserReviews = () => {
  //     fetchReview();
  //   };

  //   fetchUserReviews();
  // }, []);

  return (
    <div className="bg-gradient-to-b from-gray-200 to-gray-300 h-full p-8">
      <div className="max-w-4xl mx-auto bg-white p-8 rounded-lg shadow-lg">
        <h1 className="text-4xl font-bold text-gray-800 mb-6">Analytics</h1>

        <form
          action=""
          className="flex flex-col gap-4"
          onSubmit={handleFormSubmit}
        >
          <input
            type="text"
            placeholder="Search place"
            className="bg-gray-100 p-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-400"
            name="search"
          />
          <button className="bg-blue-500 text-white p-3 rounded-lg hover:bg-blue-600 transition">
            Submit
          </button>
        </form>

        <h1 className="text-2xl font-bold text-gray-800 mt-8">
          Analyze a Review
        </h1>
        <form
          onSubmit={handleReviewAnalysis}
          className="flex flex-col gap-4 mt-4"
        >
          <input
            type="text"
            placeholder="Enter review to analyze"
            name="review"
            className="bg-gray-100 p-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-400"
          />
          <button className="bg-green-500 text-white p-3 rounded-lg hover:bg-green-600 transition">
            Analyze
          </button>
        </form>

        <div>
          <h2 className="text-2xl font-semibold text-gray-800 mt-8">
            User Reviews
          </h2>
          <div className="h-96 overflow-y-auto bg-gray-100 p-4 rounded-lg shadow-inner mt-4">
            {user.reviews.length > 0 ? (
              <ul className="list-disc ml-8 mt-2">
                {user.reviews.map((review, index) => (
                  <li key={index} className="mb-6">
                    <p>
                      <strong>Content:</strong> {review.content}
                    </p>
                    <p>
                      <strong>Sentiment:</strong> {review.analysis.sentiment}
                    </p>
                    <p>
                      <strong>Emotion:</strong>{" "}
                      {review.analysis.emotion.join(", ")}
                    </p>
                    <p>
                      <strong>Key Themes:</strong>{" "}
                      {review.analysis.keyThemes.join(", ")}
                    </p>
                    <p>
                      <strong>Pain Points:</strong>{" "}
                      {review.analysis.painPoints.join(", ")}
                    </p>
                    <p>
                      <strong>Urgency:</strong> {review.analysis.urgency}
                    </p>
                    <p>
                      <strong>Recommendations:</strong>{" "}
                      {review.analysis.recommendation.join(", ")}
                    </p>
                    <p>
                      <strong>Timestamp:</strong>{" "}
                      {new Date(review.created_at).toLocaleString("en-US", {
                        year: "numeric",
                        month: "long",
                        day: "numeric",
                        hour: "2-digit",
                        minute: "2-digit",
                        second: "2-digit",
                      })}
                    </p>
                  </li>
                ))}
              </ul>
            ) : (
              <p className="text-gray-600">No reviews found.</p>
            )}
          </div>

          <h1 className="text-2xl font-semibold text-gray-800 mt-8">
            Overall analysis
          </h1>
          <div>
            <button onClick={findOverallAnalysis} className="cursor-pointer">
              Find the overall analysis?
            </button>
            {overallAnalysis ? <p>overallAnalysis</p> : null}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Analytics;
