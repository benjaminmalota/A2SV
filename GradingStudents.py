{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1f65d293",
   "metadata": {},
   "outputs": [],
   "source": [
    "#!/bin/python3\n",
    "\n",
    "import math\n",
    "import os\n",
    "import random\n",
    "import re\n",
    "import sys\n",
    "\n",
    "#\n",
    "# Complete the 'gradingStudents' function below.\n",
    "#\n",
    "# The function is expected to return an INTEGER_ARRAY.\n",
    "# The function accepts INTEGER_ARRAY grades as parameter.\n",
    "#\n",
    "\n",
    "def gradingStudents(grades):\n",
    "    \n",
    "    # Write your code here\n",
    "    gd = []\n",
    "    for grade in grades:\n",
    "        if grade < 38:\n",
    "            gd.append(grade)\n",
    "        elif grade % 5 > 2:\n",
    "            grade = (grade//5+1)*5\n",
    "            gd.append(grade)\n",
    "        else:\n",
    "            gd.append(grade)\n",
    "    return gd\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    fptr = open(os.environ['OUTPUT_PATH'], 'w')\n",
    "\n",
    "    grades_count = int(input().strip())\n",
    "\n",
    "    grades = []\n",
    "\n",
    "    for _ in range(grades_count):\n",
    "        grades_item = int(input().strip())\n",
    "        grades.append(grades_item)\n",
    "\n",
    "    result = gradingStudents(grades)\n",
    "\n",
    "    fptr.write('\\n'.join(map(str, result)))\n",
    "    fptr.write('\\n')\n",
    "\n",
    "    fptr.close()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
