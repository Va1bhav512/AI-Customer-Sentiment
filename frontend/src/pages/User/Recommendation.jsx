import React from "react";
import useUserStore from "../../store/userStore";

const Recommendations = () => {
  const { user } = useUserStore();

  const feedbackData = user.reviews;

  return (
    <div className="bg-[#F7FAFC] h-full p-8 rounded-xl shadow-lg">
      <h1 className="font-extrabold text-4xl text-center text-gray-800 mb-8">
        Immediate Attention Required
      </h1>

      <div className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6">
        {feedbackData.map((feedback, index) => (
          <RecommendationCard key={index} feedback={feedback} />
        ))}
      </div>
    </div>
  );
};

const RecommendationCard = ({ feedback }) => {
  const { keyThemes, urgency, recommendation } = feedback.analysis;

  const urgencyClass =
    urgency === "High"
      ? "border-red-600 border-2"
      : urgency === "Medium"
      ? "border-yellow-600 border-2"
      : "border-green-600 border-2";

  return (
    <div className={`bg-white rounded-xl p-6 shadow-lg hover:shadow-2xl transition-shadow duration-200 ${urgencyClass}`}>
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-xl font-bold text-gray-800">
          {keyThemes.join(", ")}
        </h2>
        {/* Apply urgencyClass only to the badge */}
        <span className={`px-4 py-1 rounded-full font-medium ${urgencyClass}`}>
          {urgency}
        </span>
      </div>

      <ul className="list-disc pl-5 text-gray-700 text-sm mb-4">
        {recommendation.map((rec, idx) => (
          <li key={idx} className="mb-2">
            {rec}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Recommendations;
