import axios from "axios";

const BASE_URL = "https://places.googleapis.com/v1/places:searchText";

const config = {
  headers: {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": import.meta.env.VITE_GOOGLE_API,
    "X-Goog-FieldMask": [
      "place.name",
      "place.formatted_address",
      "place.geometry",
      "place.icon",
    ],
  },
};

export const GetPlaceDetails = (data) => axios.post(BASE_URL, data, config);
