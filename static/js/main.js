function ConfirmDelete() {
  if (confirm("Are you sure you want to delete?")) {
    document.getElementById("delete-form").submit();
    return true;
  } else {
    return false;
  }
}
