import React from 'react';
import { unfollowFromJson } from './api';
import { useLocation } from 'react-router-dom';

function Confirmation() {
    const location = useLocation();
    const params = new URLSearchParams(location.search);
    const filePath = params.get('file');

    const handleUnfollow = async () => {
        const response = await unfollowFromJson(filePath);
        alert('Unfollow completed');
        console.log(response.data);
    };

    return (
        <div>
            <h2>Confirm Unfollow</h2>
            <p>File: {filePath}</p>
            <button onClick={handleUnfollow}>Unfollow Accounts</button>
        </div>
    );
}

export default Confirmation;
