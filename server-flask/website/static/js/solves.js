function deleteSolve(solveID) {
    fetch("/solves", {
        method: "DELETE",
        body: JSON.stringify({ id : solveID})
    }).then((_res) => {
        window.location.href = "/";
    });
}