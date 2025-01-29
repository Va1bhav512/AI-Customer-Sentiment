import React from "react";
import { FaSearch } from "react-icons/fa";
import { CiBellOn } from "react-icons/ci";
import { MdArrowDropDown } from "react-icons/md";

// import FOCUS_IMAGE from "/focus_image.png"; // Replace with a relevant image

const focusAreaContent = [
  {
    heading: "Customer Feedback on Product A",
    percentage: "12% Negative Feedback",
    details: "Majority of users are unhappy with the user interface.",
    type: "negative",
    action: "Prioritize UI redesign and simplify navigation.",
  },
  {
    heading: "Customer Satisfaction on Product B",
    percentage: "30% Positive Feedback",
    details: "Customers are praising the new features and performance.",
    type: "positive",
    action: "Capitalize on this positive sentiment for future marketing.",
  },
  {
    heading: "Customer Support Satisfaction",
    percentage: "18% Negative Feedback",
    details:
      "Several complaints about long wait times and unhelpful responses.",
    type: "negative",
    action: "Improve response time and training for support agents.",
  },
];

const focusMetrics = [
  {
    name: "UI Feedback",
    percentage: "40%",
    description: "Negative feedback regarding the user interface.",
  },
  {
    name: "Performance Praise",
    percentage: "30%",
    description: "Positive feedback for speed and stability.",
  },
  {
    name: "Support Issues",
    percentage: "18%",
    description: "Complaints regarding slow response times.",
  },
  {
    name: "Feature Requests",
    percentage: "12%",
    description: "Suggestions for additional features and improvements.",
  },
];

const FocusArea = () => {
  return (
    <div className="bg-[#E9F1F9] h-full p-8 rounded-lg shadow-lg">
      <h1 className="font-bold text-4xl text-gray-800">Focus Areas</h1>

      <div className="flex gap-6 mt-6 flex-wrap justify-between">
        {focusAreaContent.map((content, index) => {
          return <FocusCard key={index} content={content} />;
        })}
      </div>

      <h1 className="font-semibold text-2xl text-gray-700 mt-8">Focus Metrics</h1>

      <div className="flex gap-6 mt-6 flex-wrap justify-between">
        {focusMetrics.map((metric, index) => {
          return <FocusMetricCard key={index} metric={metric} />;
        })}
      </div>
    </div>
  );
};

const FocusCard = ({ content }) => {
  const isPositive = content.type === "positive";

  return (
    <div className="bg-white rounded-lg p-6 shadow-xl my-4 w-[30%] min-w-[280px]">
      {/* Heading */}
      <p
        className={`text-[1.25rem] font-semibold mb-2 ${
          isPositive ? "text-green-600" : "text-red-600"
        }`}
      >
        {content.heading}
      </p>

      {/* Feedback Details */}
      <div className="my-4">
        <h1
          className={`font-semibold text-xl ${
            isPositive ? "text-green-500" : "text-red-500"
          }`}
        >
          {content.percentage}
        </h1>
        <p className="text-gray-600">{content.details}</p>
      </div>

      {/* Action */}
      <div className="mt-4">
        <button
          className={`w-full py-2 px-4 rounded-lg font-semibold text-white transition-all duration-200 ease-in-out ${
            isPositive
              ? "bg-green-500 hover:bg-green-600"
              : "bg-red-500 hover:bg-red-600"
          }`}
        >
          {content.action}
        </button>
      </div>
    </div>
  );
};

const FocusMetricCard = ({ metric }) => {
  return (
    <div className="bg-white p-6 rounded-lg shadow-xl my-4 w-[30%] min-w-[280px]">
      <h1 className="text-lg font-semibold text-gray-800">{metric.name}</h1>
      <h2
        className={`font-bold text-[2rem] mt-2 ${
          metric.percentage.includes("%") && parseInt(metric.percentage) > 20
            ? "text-green-600"
            : "text-red-600"
        }`}
      >
        {metric.percentage}
      </h2>
      <p className="text-gray-500 text-sm mt-2">{metric.description}</p>
    </div>
  );
};

export default FocusArea;
