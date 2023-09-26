import React from 'react';
import data from '../assets/data.json';

const EventBox = ({ event }) => (
  <div className="bg-white shadow-lg rounded-lg w-72 p-6 m-4 flex flex-col">
    <h2 className="text-xl font-semibold mb-2 text-center">{event.name}</h2>
    <p className="text-gray-500 mb-4 text-center">
      Date: {event.startsOn} till {event.endsOn}
    </p>
    <p className="text-gray-600">{event.description}</p>
  </div>
);

const EventList = () => {
  return (
    <div className="flex flex-wrap gap-6 justify-center">
      {data.map((event, index) => (
        <EventBox key={index} event={event} />
      ))}
    </div>
  );
};

export default EventList;
