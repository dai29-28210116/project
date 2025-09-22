// src/api/attachment.js
import apiClient from "./axios";

export function fetchAttachments(params) {
  return apiClient.get("core/attachments/", { params });
}

export function uploadAttachment(file, contentTypeId, objectId, section = "main") {
  const formData = new FormData();
  formData.append("file", file);
  formData.append("content_type_id", contentTypeId); // ← 数値 ID
  formData.append("object_id", objectId);
  formData.append("section", section);            // ← 追加

  return apiClient.post("core/attachments/", formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
}

export function deleteAttachment(id) {
  return apiClient.delete(`core/attachments/${id}/`);
}
