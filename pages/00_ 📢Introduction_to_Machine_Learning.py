import streamlit as st

tab_1 , tab_2 , tab_3 , tab_4 = st.tabs(["Understanding Machine Learning", "Types of Machine Learning", "Machine Learning  Development Cycle", "Applications of Machine Learning"])

################################## Understanding Machine Learning ##################################################################
####################################################################################################################################

with tab_1:
    
    st.markdown(""" #### What is :orange[Machine Learning]? \n
                
    **:green[Artificial Intelligence]** (AI) reference to the development of computer systems able to perform tasks
    that typically require human intelligence such as visual perception, speech recognition, decision-making, and problem-solving, it encompases various 
    technologies including machine learning , natural language processing, computer vision, robotics, and many more. [1](https://www.nature.com/articles/s41586-023-06221-2)
    
    As the field of artificial intelligence (AI) progresses and its complexity increases, a variety of its applications and potential uses are emerging more clearly. 
    There are six key areas within AI that are particularly noteworthy:
    
    1. Machine Learning
    2. Deep Learning
    3. Robotics
    4. Generative AI 
    
    In this study we will focus on one  Machine Learning as one of the subset of AI.
    
    Machine Learning (ML) : Is a field of study that focuses on the design and development of algorithms that can learn from data and make decisions without being explicitly programmed.
    Its a multi-disciplinary field rooted in statistics
    
    The history of machine learning  dates back in early 20th century and has evolved significantly over the years.
    
    1. **1943**              The journey begins with the first mathematical model of the neuron presented by Walter Pitts and Warrenn Mc Culloch.
    2. **1949**              Donald Hebb publishes "The Orginization of Behavior" introducing theories on neural networks and brain activity
    3. **1950**              Alan Turing Creates the Turing Test to test to determine if a computer has real intelligence or not.
    4. **1952**              Argthur Samuel introduces the concept of **"Generalization"** in Machine Learning.
    5. **1967**              Introduction of the “nearest neighbor” algorithm for basic pattern recognition.
    6. **1979-1981**         Development of the Stanford Cart and Explanation Based Learning (EBL).
    7. **1990s**             Shift from knowledge-driven to data-driven approach in machine learning.
    8. **2006**              Geoffrey Hinton coins the term "deep learning."
    9. **2010 and beyond**   Significant advancements with IBM's Watson, Google Brain, and autonomous vehicles, among others \n
    
    For  More Detailed exploration of History of AI you can visit the full article on [Blog](https://www.techtarget.com/whatis/A-Timeline-of-Machine-Learning-History) \n
    
                
                """)


################################## Types of Machine Learning ##################################################################
###############################################################################################################################
with tab_2:
    
    st.markdown( """
    
        In the previous section we have discussed about the history of Machine Learning\n
        
        Now we will discuss about the various types of Machine Learning.
        Machine Learning can be broadly classified into three broad categories:
        
        1. Supervised Learning
        2. Unsupervised Learning
        3. Reinforcement Learning        
                
                
                """ )


    st.markdown(""" ##### What is Supervised Learning? """)
    st.markdown(""" 
                        
            :orange[Supervised Learning] : In this learning, the data is :green[labelled] and the algorithm is trained to predict the output based on the input. A Labelled data is data that contains an instances of Input Features and Target Variable.
            
            For example:
            
            A telecommunications company might have a dataset containing various customer details such as call usage, account tenure, billing information, service quality experiences,
            and additional subscribed services.The company might be interested in predicting customer churn, which refers to the likelihood of a customer discontinuing their service in the near future.
            
            In this historical dataset, there would be **Features** and a **Target**:
            
            1. *Features* would be attributes of each customer, like the duration and frequency of calls,
            length of service with the company, payment history, quality of service issues reported, types of services subscribed to (like data plans, international calling), and demographic information.

            2. The *Target* would represent whether a particular customer churned in the past. This is typically indicated by a binary value such as 1 or 0, True or False, or Yes or No, where '1' or 'True' 
            or 'Yes' would indicate that the customer had churned (discontinued the service), and '0' or 'False' or 'No' would indicate they continued with the service.

            Using this data, machine learning models can be trained to identify patterns and correlations that suggest a higher likelihood of churn. This insight enables the company to implement targeted retention
            strategies to reduce the churn rate. The target variable is the variable that is to be predicted. The features are the variables that are used to predict the target variable.
            Supervise Learing use algorithims that learn the relationship between the features and the target variable.
    
            
            Under Supervised Learning we have two types of task that are used often:
            
            1. **:green[Classification Tasks]**
            2. **:green[Regression Tasks]** \n
            
            
            
            ##### Classification Tasks :
            
        
            In general, the term **classification** refers to the process of recognizing, understanding, and grouping objects or events into predefined categories. 
            In the context of machine learning, a classification task involves the application of mathematical models and algorithms that learn patterns and comprehend 
            the relationships between features and the target variable. These models and algorithms are then used to classify new data accurately into the appropriate category.
            
            Lets example below of this picture:
        
                """
                )
    
    # cointainer = st.container(border=True)
    st.image('assets/classification.png', width=600, caption='Classification Tasks')
################################## Machine Learning Development Cycle ##################################################################
########################################################################################################################################

with tab_3:
    
    st.write('In Progress')



################################## tab 4 ##################################################################
###########################################################################################################


with tab_4:
    
    st.write('In Progress')
