
FROM ubuntu

ARG pass

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python python-pip python-dev && pip install --upgrade pip

RUN apt-get update -y && apt-get install git -y

RUN pip install pytest
RUN pip install selenium

RUN git clone https://ksanayarysh:$pass@github.com/ksanayarysh/otus-qa-course.git /otus-qa-course


WORKDIR /otus-qa-course


CMD ["/bin/bash"]
