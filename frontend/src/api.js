import axios from 'axios';

const API_BASE_URL = "https://instagram-backend-xyz.run.app"; // Replace with your Cloud Run URL

export const login = async (username, password) => {
    return await axios.post(`${API_BASE_URL}/login/`, { username, password });
};

export const fetchNonFollowers = async () => {
    return await axios.get(`${API_BASE_URL}/non-followers/`);
};

export const unfollowFromJson = async (filePath) => {
    return await axios.post(`${API_BASE_URL}/unfollow/`, null, { params: { file_path: filePath } });
};
