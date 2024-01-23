// Dashboard.js
import React, { useState, useEffect } from 'react';

const Dashboard = () => {
  const [userProfile, setUserProfile] = useState({});
  const [allProfiles, setAllProfiles] = useState([]);
  const [editMode, setEditMode] = useState(false);
  const [editedProfile, setEditedProfile] = useState({});

  useEffect(() => {
    fetchUserProfile();
    fetchAllProfiles();
  }, []);

  const fetchUserProfile = async () => {
    try {
      const response = await fetch('http://localhost:5000/dashboard/profile', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const userData = await response.json();
      setUserProfile(userData);
    } catch (error) {
      console.error('Error fetching user profile:', error.message);
    }
  };

  const fetchAllProfiles = async () => {
    try {
      const response = await fetch('http://localhost:5000/dashboard/profiles', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const profilesData = await response.json();
      setAllProfiles(profilesData.profiles);
    } catch (error) {
      console.error('Error fetching all profiles:', error.message);
    }
  };

  const handleEdit = () => {
    setEditMode(true);
    setEditedProfile({
      username: userProfile.username,
      email: userProfile.email,
    });
  };

  const handleCancelEdit = () => {
    setEditMode(false);
    setEditedProfile({});
  };

  const handleSaveEdit = async () => {
    try {
      const response = await fetch('http://localhost:5000/dashboard/profile', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(editedProfile),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      fetchUserProfile();
      setEditMode(false);
      setEditedProfile({});
    } catch (error) {
      console.error('Error updating profile:', error.message);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setEditedProfile({
      ...editedProfile,
      [name]: value,
    });
  };

  return (
    <div className="container mx-auto mt-8">
      <h1 className="text-3xl font-bold mb-4">User Dashboard</h1>

      <div className="mb-8">
        <h2 className="text-xl font-bold mb-2">Your Profile</h2>
        {editMode ? (
          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block mb-2">Username:</label>
              <input
                type="text"
                name="username"
                value={editedProfile.username}
                onChange={handleInputChange}
                className="border rounded p-2 mb-4 w-full"
              />
            </div>
            <div>
              <label className="block mb-2">Email:</label>
              <input
                type="email"
                name="email"
                value={editedProfile.email}
                onChange={handleInputChange}
                className="border rounded p-2 mb-4 w-full"
              />
            </div>
          </div>
        ) : (
          <div>
            <p>
              <strong>Username:</strong> {userProfile.username}
            </p>
            <p>
              <strong>Email:</strong> {userProfile.email}
            </p>
          </div>
        )}

        <div className="mt-4">
          {editMode ? (
            <>
              <button
                className="bg-green-500 text-white px-4 py-2 rounded mr-2 hover:bg-green-600"
                onClick={handleSaveEdit}
              >
                Save
              </button>
              <button
                className="bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600"
                onClick={handleCancelEdit}
              >
                Cancel
              </button>
            </>
          ) : (
            <button
              className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
              onClick={handleEdit}
            >
              Edit Profile
            </button>
          )}
        </div>
      </div>

      <div>
        <h2 className="text-xl font-bold mb-2">All Profiles</h2>
        <table className="min-w-full bg-white border border-gray-300">
          <thead>
            <tr>
              <th className="py-2 px-4 border-b">Username</th>
              <th className="py-2 px-4 border-b">Email</th>
            </tr>
          </thead>
          <tbody>
            {allProfiles.map((profile, index) => (
              <tr key={index} className="hover:bg-gray-100">
                <td className="py-2 px-4 border-b">{profile.username}</td>
                <td className="py-2 px-4 border-b">{profile.email}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Dashboard;
