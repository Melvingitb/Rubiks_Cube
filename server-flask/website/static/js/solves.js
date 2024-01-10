function deleteSolve(solveID) {
    fetch("/solves", {
        method: "DELETE",
        body: JSON.stringify({ id : solveID})
    }).then((_res) => {
        window.location.href = "/solves";
    });
}

function plusTwo(solveID) {
    fetch("/solves", {
        method: "PUT",
        body: JSON.stringify({ id : solveID})
    }).then((_res) => {
        window.location.href = "/solves";
    });
}