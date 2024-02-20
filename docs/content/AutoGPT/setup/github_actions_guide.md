jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout
      uses: actions/checkout@v2
    - name: Set up Git
      run: |
        git config --global user.name "GitHub Actions"
        git config --global user.email "actions@github.com"
    - name: Use GitHub Token
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      run: |
        echo "Using GitHub Token for API calls"
