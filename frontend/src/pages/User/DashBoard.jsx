import React from "react";
import { FaSearch } from "react-icons/fa";
import { CiBellOn } from "react-icons/ci";
import { MdArrowDropDown } from "react-icons/md";
import { FaEye } from "react-icons/fa";
import { IoChatboxEllipsesOutline } from "react-icons/io5";

import IPHONE from "/iphone.png";
import EXCITEMENT from "/excitement.png";
import JOY from "/joy.png";
import FRUSTRATE from "/frustrate.png";

import MARQUS from "/marqus.png";
import GURU_1 from "/guru1.png";
import GURU_2 from "/guru2.png";

import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  Radar,
} from "recharts";
import useUserStore from "../../store/userStore";

const alertContent = [
  {
    heading: "Spike in Negative Feedback Detected",
    percentage: "15%",
    percentageContent: "increase in negative comments",
    mainTakeAway: "Low Iphone battery life",
    type: "negative",
  },
  {
    heading: "Trending Topics",
    percentage: "25%",
    percentageContent: "increase in positive mentions",
    mainTakeAway: "Environmental Initiatives",
    type: "positive",
  },
];

const iphoneContent = [
  {
    image: EXCITEMENT,
    metrics: "Excitement (45%)",
    description: "Praises for titanium design and performance.",
  },
  {
    image: JOY,
    metrics: "Joy (27%)",
    description: "Positive feedback on camera quality and battery life.",
  },
  {
    image: FRUSTRATE,
    metrics: "Frustrations (5%)",
    description: "Heating during gaming and High Pricing",
  },
];

const guruContent = [
  {
    image: GURU_1,
    channel_name: "Tech Guru",
    subscribers: "3.4M",
    avg_views: "1.4M/Video",
    engagement: "24%",
    description: "Trusted in tech space",
  },
  {
    image: GURU_2,
    channel_name: "Daily Gadgets",
    subscribers: "3.2M",
    avg_views: "890K/Video",
    engagement: "18%",
    description: "Reach in Mid-Tier Markets",
  },
];

// const emotionData = [
//   { emotion: "Satisfaction", value: 0.4 },
//   { emotion: "Joy", value: 0.3 },
//   { emotion: "Disappointment", value: 0.3 },
//   { emotion: "Mild Frustration", value: 0.2 },
// ];

const DashBoard = () => {
  const { user, overAllAnalysis, fetchReview } = useUserStore();
  console.log(overAllAnalysis);

  const fluctuationData = overAllAnalysis?.Fluctuation?.map((value, index) => ({
    name: new Date(user.reviews[index].created_at).toLocaleString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
    }),
    fluctuation: value,
  }));

  const emotionData = [
    {
      emotion: "Satisfaction",
      value: overAllAnalysis["Key Emotions"]?.satisfaction,
    },
    { emotion: "Joy", value: overAllAnalysis["Key Emotions"]?.joy },
    {
      emotion: "Disappointment",
      value: overAllAnalysis["Key Emotions"]?.disappointment,
    },
    {
      emotion: "Positive",
      value: overAllAnalysis["Key Emotions"]?.["positive"],
    },
  ];

  return (
    <div className="bg-[#E9F1F9] min-h-screen p-8">
      <div className="top-bar w-full flex items-center gap-4 justify-between">
        <div className="bg-white p-3 rounded-lg w-3/5 flex items-center">
          <FaSearch className="text-black text-lg mx-3 cursor-pointer" />
          <input
            type="text"
            placeholder="Search"
            className="w-full mx-2 p-2 border-transparent focus:border-0 focus:outline-none focus:ring-0"
          />
        </div>

        {/* <button onClick={fetchReview} className="cursor-pointer bg-white p-4 rounded-lg text-bold">Fetch Reviews</button> */}

        <div className="bg-white rounded-full p-2 flex items-center justify-center cursor-pointer">
          <CiBellOn className="text-2xl text-gray-600" />
        </div>
      </div>

      <h1 className="font-extrabold text-4xl mt-8 text-gray-800">Alerts</h1>
      <div className="flex gap-8 mt-6">
        {alertContent.map((content, index) => (
          <AlertCard key={index} content={content} />
        ))}
      </div>

      <div>
        <h1 className="font-bold text-2xl">Analysis Message</h1>
        <p className="text-gray-700 text-xl">
          {overAllAnalysis["Overall Analysis"]}
        </p>
      </div>

      <div className="flex gap-8 mt-8">
        <div className="w-2/3 bg-white rounded-lg shadow-lg p-6">
          <div className="flex items-center justify-between mb-6">
            <h1 className="text-2xl font-bold text-gray-800">
              Iphone 15 Pro Max
            </h1>
            <div className="bg-gray-200 p-3 text-lg font-semibold flex items-center border-2 rounded-full cursor-pointer">
              <p>Top Product</p>
              <MdArrowDropDown />
            </div>
          </div>

          <div className="flex gap-12">
            <div className="w-auto flex items-center justify-center">
              <img
                src={IPHONE}
                alt="Iphone"
                className="w-36 h-auto rounded-lg shadow-md"
              />
            </div>

            <div className="flex gap-6 items-center justify-center flex-1">
              {iphoneContent.map((content, index) => (
                <IphoneCard key={index} content={content} />
              ))}
            </div>
          </div>
        </div>

        {/* Replace BarChart with AreaChart */}
        <div className="bg-white rounded-lg shadow-lg p-6 w-1/3">
          <h1 className="text-2xl font-bold text-gray-800 mb-6">
            Sentiment Fluctuation Graph
          </h1>
          <ResponsiveContainer width="100%" height={300}>
            <AreaChart
              data={fluctuationData}
              margin={{
                top: 5,
                right: 30,
                left: 20,
                bottom: 5,
              }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis
                dataKey="name"
                label="Time"
                tick={false} // Disables the tick labels
                tickLine={false} // Disables the tick lines (points)
                axisLine={false} // Disables the axis line itself
              />
              <YAxis />
              <Tooltip />
              <Area
                type="monotone"
                dataKey="fluctuation"
                stroke="#8884d8"
                fill="#8884d8"
              />
            </AreaChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Radar chart for emotions */}
      <div className="bg-white rounded-lg shadow-lg p-6 w-auto mt-4">
        <h1 className="text-2xl font-bold text-gray-800 mb-6">
          Emotion Sentiment Analysis
        </h1>
        <ResponsiveContainer width="100%" height={300}>
          <RadarChart cx="50%" cy="50%" outerRadius="80%" data={emotionData}>
            <PolarGrid />
            <PolarAngleAxis dataKey="emotion" />
            <PolarRadiusAxis domain={[0, 1]} />
            <Radar
              name="Emotions"
              dataKey="value"
              stroke="#8884d8"
              fill="#8884d8"
              fillOpacity={0.6}
            />
            <Tooltip />
          </RadarChart>
        </ResponsiveContainer>
      </div>

      <h1 className="text-2xl font-bold text-gray-800 mb-6 mt-6">
        YouTube Video Analysis – Engagement & Influencer Insights
      </h1>
      <div className="bg-white rounded-lg shadow-lg p-6 w-auto mt-4 flex justify-between px-12">
        <div className="flex flex-col gap-4">
          <h1 className="text-[1.5rem] font-bold">Trending Videos</h1>

          <div className="flex gap-4 items-center">
            <img src={MARQUS} alt="" />
            <div>
              <div className="flex items-center gap-4">
                <FaEye />
                <p>4.3M</p>
              </div>

              <div className="flex items-center gap-4">
                <IoChatboxEllipsesOutline />
                <p>22%</p>
              </div>
            </div>
          </div>

          <div>
            <h2 className="font-bold text-[1.15rem]">Title</h2>
            <p>An Honest review of Apple intelligence</p>
          </div>
          <div>
            <h2 className="font-bold text-[1.15rem]">Creator</h2>
            <p>Marques Brownlee</p>
          </div>
        </div>

        <div>
          <h1 className="text-[1.5rem] font-bold">Top Influencers</h1>
          <div className="flex flex-col gap-4 mt-4">
            {guruContent.map((content, index) => (
              <GuruCard key={index} content={content} />
            ))}
          </div>
        </div>

        <div className="">
          <h1 className="text-[1.5rem] font-bold">Sentiment Analysis</h1>

          <p className="p-2 border-green-500 border-2 rounded-full my-2 font-bold text-green-800">
            Performance
          </p>
          <p className="p-2 border-green-500 border-2 rounded-full my-2 font-bold text-green-800">
            Design
          </p>
          <p className="p-2 border-red-500 border-2 rounded-full my-2 font-bold text-red-800">
            Bad Song Suggestions in Apple Music
          </p>
          <p className="p-2 border-red-500 border-2 rounded-full my-2 font-bold text-red-800">
            Heating Problems
          </p>
          <p className="p-2 border-green-500 border-2 rounded-full my-2 font-bold text-green-800">
            Titanium Build
          </p>
        </div>
      </div>
    </div>
  );
};

export default DashBoard;

const AlertCard = ({ content }) => {
  const isPositive = content.type === "positive";

  return (
    <div
      className={`bg-white rounded-lg p-5 shadow-md w-full lg:w-1/3 mb-8 ${
        isPositive ? "border-l-8 border-green-500" : "border-l-8 border-red-500"
      }`}
    >
      <h3
        className={`text-xl font-semibold ${
          isPositive ? "text-green-600" : "text-red-600"
        }`}
      >
        {content.heading}
      </h3>

      <div className="flex items-center gap-6 my-4">
        <div className="flex flex-col items-center justify-center">
          <h1
            className={`text-3xl font-bold ${
              isPositive ? "text-green-600" : "text-red-600"
            }`}
          >
            {content.percentage}
          </h1>
          <p className="text-gray-500">{content.percentageContent}</p>
        </div>
        <h1 className="text-gray-800 font-medium">{content.mainTakeAway}</h1>
      </div>

      <button
        className={`p-3 w-full font-bold rounded-md ${
          isPositive
            ? "bg-green-500 text-white hover:bg-green-600"
            : "bg-red-500 text-white hover:bg-red-600"
        }`}
      >
        Nudge Product Team
      </button>
    </div>
  );
};

const IphoneCard = ({ content }) => {
  return (
    <div className="flex flex-col items-center justify-center bg-white p-4 rounded-xl shadow-lg w-32">
      <img
        src={content.image}
        alt="Iphone Metrics"
        className="w-12 h-12 object-cover rounded-full mb-4"
      />
      <h3 className="text-lg font-bold text-center text-gray-700">
        {content.metrics}
      </h3>
      <p className="text-sm text-center text-gray-500">{content.description}</p>
    </div>
  );
};

const GuruCard = ({ content }) => {
  return (
    <div className="flex gap-4 items-center p-4">
      <img
        src={content.image}
        alt={content.channel_name}
        className="w-16 h-16 rounded-full"
      />

      <div className="flex flex-col">
        <p className="font-bold text-blue-600">{content.channel_name}</p>
        <p className="text-gray-600">
          Subscribers:{" "}
          <span className="font-semibold">{content.subscribers}</span>
        </p>
        <p className="text-gray-600">
          Avg. Views: <span className="font-semibold">{content.avg_views}</span>
        </p>
        <p className="text-gray-600">
          Engagement:{" "}
          <span className="font-semibold">{content.engagement}</span>
        </p>
        <p className="text-gray-500 text-sm">{content.description}</p>
      </div>
    </div>
  );
};
