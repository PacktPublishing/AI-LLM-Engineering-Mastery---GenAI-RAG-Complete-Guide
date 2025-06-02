import os
from dotenv import find_dotenv, load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv(find_dotenv())
client = OpenAI()


def generate_milestones(task_description):

    prompt = f""" 
            Break down the following taks into smaller milestones:
            \n\nTask:
            {task_description}
            \n\n Milestones:
            
        Make sure the result is formatted as follows:
        1. **Week 1-2:** 
   - Research and select a marathon to participate in.
   - Start a basic running training program with shorter distances.
   - Purchase necessary gear such as running shoes and clothing.

2. **Week 3-8:** 
   - Increase running distance gradually to build endurance.
   - Focus on consistency with training schedule.
   - Introduce cross-training activities to improve overall fitness.

3. **Week 9-16:** 
   - Incorporate hill training and speed workouts to improve performance.
   - Practice running at the marathon race pace.
   - Pay attention to nutrition and hydration for optimal performance.

4. **Week 17-20:** 
   - Taper off training to allow the body to rest and recover before the race.
   - Create a race day plan including transportation, pre-race nutrition, and pacing strategy.
   - Visualize success and mentally prepare for the marathon.

5. **Race Day:** 
   - Execute the race day plan by pacing yourself and staying hydrated.
   - Stay focused and motivated throughout the race.
   - Celebrate your accomplishment after finishing the marathon.

        """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a very efficient, task-driven and successful person. You have helped millions of people to become more productive and able to accomplish their most important goals in life.",
                },
                {
                    "role": "user",
                    "content": f"{prompt}",
                },
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"


def app_console():
    print("Task Breakdown Generator")
    task_description = input(
        "Enter the task or goal you'd like to break down into milestones:"
    )

    if task_description:
        print("\nGenerating milestones...")
        milestones = generate_milestones(task_description)
        if milestones:
            print("\nMilestones:")
            print(milestones)
        else:
            print("Failed to generate milestones")
    else:
        print("No task description provided.")


def streamlit_app():
    st.title("Task Breakdown App")

    task_description = st.text_area(
        "Enter the task or goal you'd like to break down into milestones:"
    )
    if st.button("Generate Milestones"):
        if task_description:
            milestones = generate_milestones(task_description)
            st.markdown("### Milestones")
            st.write(milestones)
        else:
            st.write("Please enter a task description")


def main():
    streamlit_app()
    # app_console()


if __name__ == "__main__":
    main()
