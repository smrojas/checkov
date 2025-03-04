# flake8: noqa
terms = [
    "\${{ github.event.issue.title }}",
    "\${{ github.event.issue.body }}",
    "\${{ github.event.pull_request.title }}",
    "\${{ github.event.pull_request.body }}",
    "\${{ github.event.comment.body }}",
    "\${{ github.event.review.body }}",
    "\${{ github.event.review_comment.body }}",
    "\${{ github.event.pages.*.page_name}}",
    "\${{ github.event.head_commit.message }}",
    "\${{ github.event.head_commit.author.email }}",
    "\${{ github.event.head_commit.author.name }}",
    "\${{ github.event.commits.*.author.email }}",
    "\${{ github.event.commits.*.author.name }}",
    "\${{ github.event.pull_request.head.ref }}",
    "\${{ github.event.pull_request.head.label }}",
    "\${{ github.event.pull_request.head.repo.default_branch }}",
    "\${{ github.head_ref }}"
]
